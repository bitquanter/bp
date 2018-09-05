# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BigInteger, JSON, TIMESTAMP, Float, Text, DECIMAL, DateTime, BINARY
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json

# 创建对象的基类:
Base = declarative_base()


class DacComponentAdjust(Base):
    __tablename__ = 'dac_component_adjust'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dac_id = Column(BigInteger,nullable=False, doc="基金id")
    status = Column(String(32),nullable=True, doc="状态")
    old_coin_component = Column(Text,nullable=True, doc="旧的货币组合")
    old_component_type = Column(String(32),nullable=True, doc="旧组合类型")
    new_coin_component = Column(Text,nullable=True, doc="新货币组合")
    new_component_type = Column(String(32),nullable=True, doc="新组合类型")
    dac_amount = Column(DECIMAL(30,10),nullable=True, doc="基金份额")
    effective_from = Column(TIMESTAMP,nullable=True, doc="起始时间")
    effective_to = Column(TIMESTAMP,nullable=True, doc="结束时间")
    created_by = Column(String(64),nullable=True, doc="创建人")
    created_at = Column(TIMESTAMP,nullable=True, doc="创建时间")
    notes = Column(String(255),nullable=True, doc="备注")


class DacComponentWorkflow(Base):
    __tablename__ = 'dac_component_workflow'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dac_id = Column(BINARY,nullable=True, doc="基金编号")
    dac_adjust_id = Column(BigInteger,nullable=False,default=0, doc="调仓号")
    base_currency = Column(String(32),nullable=True, doc="基础货币")
    base_currency_num = Column(DECIMAL(20,10),nullable=True, doc="基础货币数量")
    trade_currency = Column(String(32),nullable=True, doc="交易货币")
    trade_currency_num = Column(DECIMAL(20,10),nullable=True, doc="交易货币数量")
    adjust_date = Column(TIMESTAMP,nullable=True,doc="调仓日期")
    notes = Column(String(255),nullable=True,doc="备注")


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
