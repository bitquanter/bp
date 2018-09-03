# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BigInteger, JSON, TIMESTAMP, Float, Text, DECIMAL, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json

# 创建对象的基类:
Base = declarative_base()

class DacComponentAdjust(Base):
    __tablename__ = 'dac_component_adjust'
    id = Column(Integer, primary_key=True, nullable= autoincrement=True)
    dac_id = Column(BigInteger, doc="基金id")
    status = Column(String(60), doc="批号")
    old_coin_component = Column(String(20), doc="buy/sell")
    old_component_type = Column(DECIMAL(30,10), doc="交易的基金的份数")
    new_coin_component = Column(String(20), doc="buy/sell")
    new_component_type = Column(DECIMAL(30,10), doc="交易的基金的份数")
    dac_amount = Column(Integer, default=0, doc="0:处理中1:批次失败2:批次成功")
    effective_from = Column(DECIMAL(30,10),default=0.0, doc="该批次总共入账的base_currency")
    effective_to = Column(Text, doc="每份基金包含的币种组成及数量")
    created_by = Column(TIMESTAMP, doc="创建时间")
    created_at = Column(TIMESTAMP, doc="更新时间")
    notes = Column(TIMESTAMP, doc="更新时间")

    def __repr__(self):
        return "<FundExchangeOrder(id={}, dac_id:{}, batch_no={}, fund_direction={}, fund_amount={}, base_currency={}, status={}, total_income_base_currency={}, component={}, created_at={}, updated_at={})>"\
            .format(self.id, self.dac_id, self.batch_no, self.fund_direction, self.fund_amount, self.base_currency, self.status, self.total_income_base_currency, self.component,  self.created_at, self.updated_at)

class DacComponentWorkflow(Base):
    __tablename__ = 'dac_component_workflow'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    dac_id = Column(BigInteger, doc="基金编号")
    batch_no = Column(String(60), doc="批号")
    trade_currency = Column(String(10), doc="eos for eos/btc")
    base_currency = Column(String(10), doc="usdt for eos/usdt")
    exchange = Column(String(20), doc="交易所:huobi/okex等")
    order_side = Column(String(20), doc="buy/sell")
    order_type = Column(String(20), doc="market/limit")
    calc_amount = Column(DECIMAL(30,10), doc="计算得到的理论下单数量")
    amount = Column(DECIMAL(30,10), doc="限价单表示下单数量，市价买单时表示买多少钱，市价卖单时表示卖多少币。交易所真实下单数量")
    price = Column(DECIMAL(30,10), doc="限价单表示价格")
    status = Column(Integer, default=0, doc="0:未提交,1:提交中,2:已提交,3:部分成交,4:完全成交,5:部分成交撤销,6:完全撤销,-1:下单失败,100:未知错误")
    submitting_at = Column(DateTime, doc="订单向交易所提交时间，纠错用")
    is_finished = Column(Integer, default=0, doc="是否结束,true if in (4:完全成交,5:部分成交撤销,6:完全撤销)")
    exchange_order_id = Column(String(100), doc="交易所订单号")
    net_incoming_trade_currency = Column(DECIMAL(30,10), doc="trade_currency实际交易量(扣除手续费)")
    net_incoming_base_currency = Column(DECIMAL(30,10), doc="base_currency实际交易量(扣除手续费)")
    avg_price = Column(DECIMAL(30,10), doc="")
    filled_amount = Column(DECIMAL(30,10), doc="成交数量")
    filled_cash_amount = Column(DECIMAL(30,10), doc="成交金额")
    filled_fees = Column(DECIMAL(30,10), doc="成交手续费")
    created_at = Column(TIMESTAMP, doc="创建时间")
    updated_at = Column(TIMESTAMP, doc="更新时间")

    def __repr__(self):
        return "<ExchangeSubOrder(id={}, dac_id={}, batch_no={}, order_type={}, order_side={}, trade_currency={}, base_currency={}, amount={}, price={}, exchange={}, status={}, submitting_at={}, is_finished={}, exchange_order_id={}, net_incoming_trade_currency={}, net_incoming_base_currency={}, avg_price={}, filled_amount={}, filled_cash_amount={}, filled_fees={}, created_at={}, updated_at={})>"\
            .format(self.id, self.dac_id, self.batch_no, self.order_type, self.order_side, self.trade_currency, self.base_currency, self.amount, self.price, self.exchange, self.status, self.submitting_at, self.is_finished, self.exchange_order_id, self.net_incoming_trade_currency, self.net_incoming_base_currency, self.avg_price, self.filled_amount, self.filled_cash_amount, self.filled_fees, self.created_at, self.updated_at)

class BpTraderDbUtil(object):
    def __init__(self, mode='dev'):
        if 'beta' == mode:
            # 准生产环境
            self.engine = create_engine(
                "mysql+pymysql://bitup:Ne88t9g7uSWVd]b@172.31.15.20:4423/bitup_sys?charset=utf8", pool_size=8,
                max_overflow=2, encoding='utf-8')
        elif 'prod' == mode:
            # 生产环境
            self.engine = create_engine(
                "mysql+pymysql://bitup:Ne88t9g7uSWVd]b@172.31.11.204:4423/bitup_sys?charset=utf8", pool_size=8,
                max_overflow=2, encoding='utf-8')
        else:
            # dev as default
            self.engine = create_engine(
                "mysql+pymysql://bitup:Ne88t9g7uSWVd]b@54.95.38.134:4423/bitup_sys?charset=utf8", pool_size=8,
                max_overflow=2, encoding='utf-8')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def fund_exchange_order_insert(self, dac_id, batch_no, fund_direction, fund_amount, base_currency, component_dict):
        component = json.dumps(component_dict)
        order_obj = FundExchangeOrder(dac_id=dac_id, batch_no=batch_no, fund_direction=fund_direction, fund_amount=fund_amount,
                                      base_currency=base_currency, component=component)
        self.session.add(order_obj)
        self.session.commit()
        return order_obj.id

    def fund_exchange_order_update_status_n_amount(self, id, status, total_income_base_currency):
        order_obj = self.session.query(FundExchangeOrder).filter_by(id=id).first()
        order_obj.status = status
        order_obj.total_income_base_currency = total_income_base_currency
        self.session.commit()

    def fund_exchange_order_get_by_batchno(self, batch_no):
        return self.session.query(FundExchangeOrder).filter_by(batch_no=batch_no).all()



    ################################################

    def exchange_suborder_insert(self, dac_id, batch_no, trade_currency, base_currency, exchange, order_side, order_type, calc_amount):
        # 到交易所下单前insert
        suborder_obj = ExchangeSubOrder(dac_id=dac_id, batch_no=batch_no, trade_currency=trade_currency, base_currency=base_currency,
                                        exchange=exchange, order_side=order_side, order_type=order_type, calc_amount=calc_amount)
        self.session.add(suborder_obj)
        self.session.commit()
        return suborder_obj.id

    def exchange_suborder_insert_direct_success_order(self, dac_id, batch_no, trade_currency, base_currency, exchange, order_side, order_type,
                                 calc_amount):
        # 对于trade_currency == base_currency的订单， status 直接是4 完全成交
        suborder_obj = ExchangeSubOrder(dac_id=dac_id, batch_no=batch_no, trade_currency=trade_currency, base_currency=base_currency,
                                        exchange=exchange, order_side=order_side, order_type=order_type,
                                        calc_amount=calc_amount, status=4, is_finished=1,
                                        net_incoming_trade_currency=calc_amount, net_incoming_base_currency=calc_amount)
        self.session.add(suborder_obj)
        self.session.commit()
        return suborder_obj.id

    def exchange_suborder_insert_neworder(self, dac_id, batch_no, suborder_db_data):
        # 到交易所下单前insert
        suborder_obj = ExchangeSubOrder(dac_id=dac_id, batch_no=batch_no, trade_currency=suborder_db_data['trade_currency'], base_currency=suborder_db_data['base_currency'],
                                        exchange=suborder_db_data['exchange'], order_side=suborder_db_data['order_side'], order_type=suborder_db_data['order_type'],
                                        calc_amount=suborder_db_data['calc_amount'], amount=suborder_db_data['amount'], price=suborder_db_data['price'],
                                        status=suborder_db_data['status'], exchange_order_id=suborder_db_data['exchange_order_id'])
        self.session.add(suborder_obj)
        self.session.commit()
        return suborder_obj.id

    def exchange_suborder_insert_neworder_before_trade(self, dac_id, batch_no, suborder_db_data):
        # 到交易所下单前insert
        suborder_obj = ExchangeSubOrder(dac_id=dac_id, batch_no=batch_no, trade_currency=suborder_db_data['trade_currency'], base_currency=suborder_db_data['base_currency'],
                                        exchange=suborder_db_data['exchange'], order_side=suborder_db_data['order_side'], order_type=suborder_db_data['order_type'],
                                        calc_amount=suborder_db_data['calc_amount'])
        self.session.add(suborder_obj)
        self.session.commit()
        return suborder_obj.id

    def exchange_suborder_update_after_trade(self, id, amount, price, exchange_order_id, status):
        suborder_obj = self.session.query(ExchangeSubOrder).filter_by(id=id).first()
        suborder_obj.amount = amount
        suborder_obj.price = price
        suborder_obj.exchange_order_id = exchange_order_id
        suborder_obj.status = status
        self.session.commit()

    def exchange_suborder_update_status_trade_fail(self, id, amount):
        # status -1:下单失败
        # is_finished: 不处理，false，未结束
        suborder_obj = self.session.query(ExchangeSubOrder).filter_by(id=id).first()
        suborder_obj.status = -1
        suborder_obj.amount = amount
        self.session.commit()

    def exchange_suborder_update_status_n_amount(self, id, status, is_finished, suborder_filled_info_dict):
        # status 0:未提交1:提交中2:已提交,3:部分成交,4:完全成交,5:部分成交撤销,6:完全撤销, 100:未知失败
        # is_finished: 是否结束,true if in(4:完全成交,5:部分成交撤销,6:完全撤销)
        # suborder_filled_info_dict: net_incoming_trade_currency, net_incoming_base_currency, avg_price, filled_amount, filled_cash_amount, filled_fees
        suborder_obj = self.session.query(ExchangeSubOrder).filter_by(id=id).first()
        suborder_obj.status = status
        suborder_obj.is_finished = is_finished
        suborder_obj.net_incoming_trade_currency = suborder_filled_info_dict['net_incoming_trade_currency']
        suborder_obj.net_incoming_base_currency = suborder_filled_info_dict['net_incoming_base_currency']
        suborder_obj.avg_price = suborder_filled_info_dict['avg_price']
        suborder_obj.filled_amount = suborder_filled_info_dict['filled_amount']
        suborder_obj.filled_cash_amount = suborder_filled_info_dict['filled_cash_amount']
        suborder_obj.filled_fees = suborder_filled_info_dict['filled_fees']
        self.session.commit()

    def exchange_suborder_update_status_finish(self, id, status):
        # is_finished -> 1
        suborder_obj = self.session.query(ExchangeSubOrder).filter_by(id=id).first()
        suborder_obj.status = status
        suborder_obj.is_finished = 1
        self.session.commit()

    def exchange_suborder_update_status_unknown(self, id):
        # status 100:未知失败
        # is_finished: 不处理，false，未结束
        suborder_obj = self.session.query(ExchangeSubOrder).filter_by(id=id).first()
        suborder_obj.status = 100
        self.session.commit()

    def exchange_suborder_get_by_batchno(self, batch_no):
        return self.session.query(ExchangeSubOrder).filter_by(batch_no=batch_no).all()

