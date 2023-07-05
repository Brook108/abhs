			
				HTML
					
					
				
				
						
				
			
		ReqOrderInsert()
函数ID: N_2293分支数: 0分支覆盖率: --调用链：
ReqOrderInsert()->Run()
Run()
函数ID: N_2428分支数: 64分支覆盖率: 45.31%调用链：
Run()->SetOrderIndex()->DistinguishBusin()->DistinguishBusin()->GetBasicData()->GetBasicData()->SendToUnionRisk()->SendToUnionRisk()->CheckBusiness()->CheckBusiness()->CalcBusinData()->CalcBusinData()->GetEntrustBalance()->GetEntrustBalance()->InsertRiskEntrust()->InsertRiskEntrust()->UpdateRiskData()->UpdateRiskData()->CheckEnable()->CheckEnable()->CheckRisk()->CheckRisk()->UpdateTempTotalFrozen()->UpdateTempTotalFrozen()->SetErrorNo()->UpdateBusinData()->UpdateBusinData()->OfferOrder()->OfferOrder()->WriteBusinToDBRedo()->WriteBusinToDBRedo()->WriteSyncRedo()->WriteSyncRedo()->RollBackRiskData()->RollBackRiskData()->SetResponse()->SetResponse()
SetOrderIndex()
函数ID: N_2861分支数: 0分支覆盖率: --调用链：
SetOrderIndex()->
DistinguishBusin()
函数ID: N_3020分支数: 0分支覆盖率: --调用链：
DistinguishBusin()->
DistinguishBusin()
函数ID: N_2830分支数: 0分支覆盖率: --调用链：
DistinguishBusin()->
GetBasicData()
函数ID: N_3021分支数: 2分支覆盖率: 50.00%调用链：
GetBasicData()->GetEtfBasicInfoByEtfCode()->GetHoldRealByCode()->GetInstanceHold()->GetStockCode()
GetEtfBasicInfoByEtfCode()
函数ID: N_1595分支数: 2分支覆盖率: 100.00%调用链：
GetEtfBasicInfoByEtfCode()->
GetHoldRealByCode()
函数ID: N_1541分支数: 2分支覆盖率: 100.00%调用链：
GetHoldRealByCode()->
GetInstanceHold()
函数ID: N_42分支数: 4分支覆盖率: 0.00%调用链：
GetInstanceHold()->GetExchangeIndex()->GetInstanceHoldByCode()->NewInstanceHold()
GetExchangeIndex()
函数ID: N_8分支数: 22分支覆盖率: 72.73%调用链：
GetExchangeIndex()->
GetInstanceHoldByCode()
函数ID: N_1560分支数: 2分支覆盖率: 100.00%调用链：
GetInstanceHoldByCode()->
NewInstanceHold()
函数ID: N_1559分支数: 2分支覆盖率: 50.00%调用链：
NewInstanceHold()->
GetStockCode()
函数ID: N_1587分支数: 2分支覆盖率: 100.00%调用链：
GetStockCode()->
GetBasicData()
函数ID: N_2831分支数: 0分支覆盖率: --调用链：
GetBasicData()->
SendToUnionRisk()
函数ID: N_2856分支数: 8分支覆盖率: 0.00%调用链：
SendToUnionRisk()->GetSerialInfo()->GetEntrustSerialNo()->GetSeatByIndex()->ConvertDouble()
GetSerialInfo()
函数ID: N_1272分支数: 0分支覆盖率: --调用链：
GetSerialInfo()->
GetEntrustSerialNo()
函数ID: N_1507分支数: 2分支覆盖率: 50.00%调用链：
GetEntrustSerialNo()->
GetSeatByIndex()
函数ID: N_1283分支数: 6分支覆盖率: 50.00%调用链：
GetSeatByIndex()->GetRecordCount()
GetRecordCount()
函数ID: N_243分支数: 0分支覆盖率: --调用链：
GetRecordCount()->
ConvertDouble()
函数ID: N_274分支数: 0分支覆盖率: --调用链：
ConvertDouble()->
SendToUnionRisk()
函数ID: N_1501分支数: 0分支覆盖率: --调用链：
SendToUnionRisk()->
CheckBusiness()
函数ID: N_3022分支数: 0分支覆盖率: --调用链：
CheckBusiness()->CheckCreationredemType()->CheckCreationredemNum()
CheckCreationredemType()
函数ID: N_3023分支数: 6分支覆盖率: 33.33%调用链：
CheckCreationredemType()->
CheckCreationredemNum()
函数ID: N_3024分支数: 4分支覆盖率: 50.00%调用链：
CheckCreationredemNum()->
CheckBusiness()
函数ID: N_2832分支数: 4分支覆盖率: 50.00%调用链：
CheckBusiness()->CHeckPriceType()->CheckStockStop()->CHeckMarketOrderCommand()->CheckOrderPriceLimit()->CheckPriceInterval()->ConvertDouble()->CheckSTBoardOrderAmountAndUnit()->CheckOrderAmountLimit()->CheckOrderUnit()
CHeckPriceType()
函数ID: N_39分支数: 12分支覆盖率: 25.00%调用链：
CHeckPriceType()->
CheckStockStop()
函数ID: N_23分支数: 2分支覆盖率: 50.00%调用链：
CheckStockStop()->
CHeckMarketOrderCommand()
函数ID: N_24分支数: 8分支覆盖率: 25.00%调用链：
CHeckMarketOrderCommand()->
CheckOrderPriceLimit()
函数ID: N_18分支数: 4分支覆盖率: 50.00%调用链：
CheckOrderPriceLimit()->
CheckPriceInterval()
函数ID: N_19分支数: 8分支覆盖率: 50.00%调用链：
CheckPriceInterval()->
CheckSTBoardOrderAmountAndUnit()
函数ID: N_20分支数: 24分支覆盖率: 0.00%调用链：
CheckSTBoardOrderAmountAndUnit()->GetSysParamVal()->operator()()->CheckOrderAmountLimit()
GetSysParamVal()
函数ID: N_1306分支数: 2分支覆盖率: 50.00%调用链：
GetSysParamVal()->
operator()()
函数ID: N_21分支数: 12分支覆盖率: 0.00%调用链：
operator()()->
CheckOrderAmountLimit()
函数ID: N_22分支数: 6分支覆盖率: 33.33%调用链：
CheckOrderAmountLimit()->
CheckOrderUnit()
函数ID: N_25分支数: 34分支覆盖率: 2.94%调用链：
CheckOrderUnit()->GetSysParamVal()->operator()()
operator()()
函数ID: N_26分支数: 12分支覆盖率: 0.00%调用链：
operator()()->
CalcBusinData()
函数ID: N_3026分支数: 0分支覆盖率: --调用链：
CalcBusinData()->ConvertInt()
ConvertInt()
函数ID: N_273分支数: 26分支覆盖率: 50.00%调用链：
ConvertInt()->
CalcBusinData()
函数ID: N_2833分支数: 2分支覆盖率: 50.00%调用链：
CalcBusinData()->CalcFee()->GetEntrustDirectionIndex()
CalcFee()
函数ID: N_14分支数: 44分支覆盖率: 45.45%调用链：
CalcFee()->GetStockFeeMgr()->GetStockFees()->getStockFeeType()->ConvertDouble()->ConvertInt()
GetStockFeeMgr()
函数ID: N_1703分支数: 2分支覆盖率: 50.00%调用链：
GetStockFeeMgr()->
GetStockFees()
函数ID: N_1636分支数: 8分支覆盖率: 100.00%调用链：
GetStockFees()->ChangeStockFeeTypeToInt()->GetFirstsHashKey()->GetSecondsHashKey()->GetStockFee()
ChangeStockFeeTypeToInt()
函数ID: N_6分支数: 8分支覆盖率: 12.50%调用链：
ChangeStockFeeTypeToInt()->
GetFirstsHashKey()
函数ID: N_321分支数: 0分支覆盖率: --调用链：
GetFirstsHashKey()->
GetSecondsHashKey()
函数ID: N_322分支数: 0分支覆盖率: --调用链：
GetSecondsHashKey()->
GetStockFee()
函数ID: N_1639分支数: 12分支覆盖率: 75.00%调用链：
GetStockFee()->GetFirstsHashKey()->operator()()
operator()()
函数ID: N_1640分支数: 4分支覆盖率: 100.00%调用链：
operator()()->GetSecondsHashKey()
getStockFeeType()
函数ID: N_13分支数: 2分支覆盖率: 50.00%调用链：
getStockFeeType()->
GetEntrustDirectionIndex()
函数ID: N_5分支数: 12分支覆盖率: 66.67%调用链：
GetEntrustDirectionIndex()->
GetEntrustBalance()
函数ID: N_2407分支数: 0分支覆盖率: --调用链：
GetEntrustBalance()->
GetEntrustBalance()
函数ID: N_2834分支数: 0分支覆盖率: --调用链：
GetEntrustBalance()->
InsertRiskEntrust()
函数ID: N_3036分支数: 4分支覆盖率: 50.00%调用链：
InsertRiskEntrust()->GetSerialInfo()->GetRiskSerialNo()->NewRiskEntrust()->ConvertInt()
GetRiskSerialNo()
函数ID: N_1487分支数: 2分支覆盖率: 50.00%调用链：
GetRiskSerialNo()->GetRiskSerialNo()->GetSerialInfo()
GetRiskSerialNo()
函数ID: N_1521分支数: 2分支覆盖率: 50.00%调用链：
GetRiskSerialNo()->
NewRiskEntrust()
函数ID: N_1767分支数: 6分支覆盖率: 50.00%调用链：
NewRiskEntrust()->SetRiskEntrust()
SetRiskEntrust()
函数ID: N_1519分支数: 10分支覆盖率: 20.00%调用链：
SetRiskEntrust()->GetRecordCount()
InsertRiskEntrust()
函数ID: N_2835分支数: 48分支覆盖率: 4.17%调用链：
InsertRiskEntrust()->GetSerialInfo()->GetRiskSerialNo()->NewRiskEntrust()->GetExchangeIndex()->GetSecurityInfo()->GetExcharg()->InsertEntrust()->GetSysParamVal()->GetSysParamVal()
GetSecurityInfo()
函数ID: N_1589分支数: 2分支覆盖率: 100.00%调用链：
GetSecurityInfo()->
GetExcharg()
函数ID: N_1277分支数: 0分支覆盖率: --调用链：
GetExcharg()->
InsertEntrust()
函数ID: N_2603分支数: 8分支覆盖率: 37.50%调用链：
InsertEntrust()->Lock()->Unlock()
Lock()
函数ID: N_2588分支数: 2分支覆盖率: 50.00%调用链：
Lock()->
Unlock()
函数ID: N_2589分支数: 0分支覆盖率: --调用链：
Unlock()->
GetSysParamVal()
函数ID: N_1303分支数: 2分支覆盖率: 50.00%调用链：
GetSysParamVal()->
GetSysParamVal()
函数ID: N_1304分支数: 2分支覆盖率: 0.00%调用链：
GetSysParamVal()->
UpdateRiskData()
函数ID: N_3038分支数: 4分支覆盖率: 50.00%调用链：
UpdateRiskData()->GetSecurityInfo()->Clear()->RiskETFOrderUpdate()
Clear()
函数ID: N_381分支数: 0分支覆盖率: --调用链：
Clear()->
RiskETFOrderUpdate()
函数ID: N_3535分支数: 0分支覆盖率: --调用链：
RiskETFOrderUpdate()->RiskOrderUpdateByLayer()
RiskOrderUpdateByLayer()
函数ID: N_3528分支数: 90分支覆盖率: 14.44%调用链：
RiskOrderUpdateByLayer()->GetRuleStockHold()->RiskUpdateOrder()->GetTradebalanceSum()->TBUpdateOpr()->GetStockType()->RiskUpdateOrder()->GetTradebalanceSum()->GetTradebalanceSum()->GetTradebalanceSum()->GetRuleStockHold()->RiskUpdateOrderVirtualGroup()->GetTradebalanceSum()->GetStockType()
GetRuleStockHold()
函数ID: N_1566分支数: 6分支覆盖率: 66.67%调用链：
GetRuleStockHold()->
RiskUpdateOrder()
函数ID: N_5455分支数: 8分支覆盖率: 37.50%调用链：
RiskUpdateOrder()->Lock()->BuyHoldCostCal()->SellHoldCostCal()->Unlock()
Lock()
函数ID: N_2193分支数: 4分支覆盖率: 75.00%调用链：
Lock()->
BuyHoldCostCal()
函数ID: N_5442分支数: 0分支覆盖率: --调用链：
BuyHoldCostCal()->HoldCostPriceCal()
HoldCostPriceCal()
函数ID: N_5441分支数: 2分支覆盖率: 50.00%调用链：
HoldCostPriceCal()->
SellHoldCostCal()
函数ID: N_5440分支数: 0分支覆盖率: --调用链：
SellHoldCostCal()->HoldCostPriceCal()
Unlock()
函数ID: N_2194分支数: 4分支覆盖率: 75.00%调用链：
Unlock()->
GetTradebalanceSum()
函数ID: N_1569分支数: 4分支覆盖率: 75.00%调用链：
GetTradebalanceSum()->
TBUpdateOpr()
函数ID: N_3523分支数: 2分支覆盖率: 50.00%调用链：
TBUpdateOpr()->OrderUpdate()
OrderUpdate()
函数ID: N_1475分支数: 6分支覆盖率: 83.33%调用链：
OrderUpdate()->
GetStockType()
函数ID: N_1563分支数: 4分支覆盖率: 75.00%调用链：
GetStockType()->
RiskUpdateOrder()
函数ID: N_5428分支数: 6分支覆盖率: 50.00%调用链：
RiskUpdateOrder()->Lock()->Unlock()
Lock()
函数ID: N_2183分支数: 2分支覆盖率: 50.00%调用链：
Lock()->
Unlock()
函数ID: N_2184分支数: 4分支覆盖率: 50.00%调用链：
Unlock()->
GetTradebalanceSum()
函数ID: N_345分支数: 4分支覆盖率: 75.00%调用链：
GetTradebalanceSum()->
GetTradebalanceSum()
函数ID: N_2236分支数: 2分支覆盖率: 0.00%调用链：
GetTradebalanceSum()->
GetTradebalanceSum()
函数ID: N_2239分支数: 2分支覆盖率: 0.00%调用链：
GetTradebalanceSum()->
GetRuleStockHold()
函数ID: N_2225分支数: 6分支覆盖率: 0.00%调用链：
GetRuleStockHold()->
RiskUpdateOrderVirtualGroup()
函数ID: N_5453分支数: 8分支覆盖率: 0.00%调用链：
RiskUpdateOrderVirtualGroup()->Lock()->Unlock()
GetTradebalanceSum()
函数ID: N_2220分支数: 0分支覆盖率: --调用链：
GetTradebalanceSum()->GetTradebalanceSumByKey()
GetTradebalanceSumByKey()
函数ID: N_2221分支数: 4分支覆盖率: 0.00%调用链：
GetTradebalanceSumByKey()->
GetStockType()
函数ID: N_2219分支数: 4分支覆盖率: 0.00%调用链：
GetStockType()->
UpdateRiskData()
函数ID: N_2836分支数: 0分支覆盖率: --调用链：
UpdateRiskData()->GetSecurityInfo()->GetPreSumFlag()->RiskOrderUpdate()
GetPreSumFlag()
函数ID: N_2152分支数: 0分支覆盖率: --调用链：
GetPreSumFlag()->lock()->unlock()
lock()
函数ID: N_357分支数: 0分支覆盖率: --调用链：
lock()->
unlock()
函数ID: N_358分支数: 0分支覆盖率: --调用链：
unlock()->
RiskOrderUpdate()
函数ID: N_3527分支数: 2分支覆盖率: 50.00%调用链：
RiskOrderUpdate()->RiskOrderUpdateByLayer()
CheckEnable()
函数ID: N_3031分支数: 0分支覆盖率: --调用链：
CheckEnable()->CheckFundEnable()
CheckFundEnable()
函数ID: N_3033分支数: 24分支覆盖率: 29.17%调用链：
CheckFundEnable()->CheckSingleFundEnable()
CheckSingleFundEnable()
函数ID: N_3044分支数: 4分支覆盖率: 50.00%调用链：
CheckSingleFundEnable()->CalcCashEnableValue()->UpdateCashEnableValueAndCashFactor()
CalcCashEnableValue()
函数ID: N_55分支数: 2分支覆盖率: 50.00%调用链：
CalcCashEnableValue()->GetCashEnableFormulaHashKey()->GetCashEnableCfgFieldByKey()->CalcCashEnableValueTN()
GetCashEnableFormulaHashKey()
函数ID: N_53分支数: 0分支覆盖率: --调用链：
GetCashEnableFormulaHashKey()->
GetCashEnableCfgFieldByKey()
函数ID: N_1731分支数: 2分支覆盖率: 50.00%调用链：
GetCashEnableCfgFieldByKey()->
CalcCashEnableValueTN()
函数ID: N_56分支数: 4分支覆盖率: 25.00%调用链：
CalcCashEnableValueTN()->GetNextNTradeDay()
GetNextNTradeDay()
函数ID: N_1739分支数: 12分支覆盖率: 91.67%调用链：
GetNextNTradeDay()->
UpdateCashEnableValueAndCashFactor()
函数ID: N_59分支数: 8分支覆盖率: 50.00%调用链：
UpdateCashEnableValueAndCashFactor()->GetCashEnableFormulaHashKey()->GetCashEnableCfgFieldByKey()->GetNextNTradeDay()->GetCashEnableFactorField()
GetCashEnableFactorField()
函数ID: N_1533分支数: 2分支覆盖率: 100.00%调用链：
GetCashEnableFactorField()->NewCashEnableFactorField()
NewCashEnableFactorField()
函数ID: N_1537分支数: 2分支覆盖率: 50.00%调用链：
NewCashEnableFactorField()->
CheckEnable()
函数ID: N_2837分支数: 12分支覆盖率: 16.67%调用链：
CheckEnable()->CalcCashEnableValue()->CheckStockEnable()->CheckInsHoldEnable()
CheckStockEnable()
函数ID: N_16分支数: 4分支覆盖率: 0.00%调用链：
CheckStockEnable()->itoa()
itoa()
函数ID: N_5517分支数: 10分支覆盖率: 0.00%调用链：
itoa()->
CheckInsHoldEnable()
函数ID: N_17分支数: 6分支覆盖率: 0.00%调用链：
CheckInsHoldEnable()->GetStockCode()
GetStockCode()
函数ID: N_1280分支数: 0分支覆盖率: --调用链：
GetStockCode()->
CheckRisk()
函数ID: N_3034分支数: 8分支覆盖率: 37.50%调用链：
CheckRisk()->clear()->RiskCheck()
clear()
函数ID: N_366分支数: 0分支覆盖率: --调用链：
clear()->clear()
clear()
函数ID: N_1152分支数: 0分支覆盖率: --调用链：
clear()->
RiskCheck()
函数ID: N_6539分支数: 4分支覆盖率: 75.00%调用链：
RiskCheck()->RiskCheck()
RiskCheck()
函数ID: N_6534分支数: 2分支覆盖率: 50.00%调用链：
RiskCheck()->ClearFlags()->CalcRuleCountPerGroup()->RuleProcess()->GetMutithreadFrameObj()->OrderCheckResult()
ClearFlags()
函数ID: N_6535分支数: 4分支覆盖率: 100.00%调用链：
ClearFlags()->
CalcRuleCountPerGroup()
函数ID: N_6536分支数: 20分支覆盖率: 60.00%调用链：
CalcRuleCountPerGroup()->
RuleProcess()
函数ID: N_6538分支数: 24分支覆盖率: 33.33%调用链：
RuleProcess()->RuleProcess()->MutexRuleQueue()->MutexRuleProcessStart()
RuleProcess()
函数ID: N_3091分支数: 6分支覆盖率: 66.67%调用链：
RuleProcess()->GetRuleProcessorIndex()->GetMutithreadFrameObj()->GetCurrectRecordHeader()->GetThreadNo()->GetMaxRecordThreadCount()->ProcessGroupRuleInRF()
GetRuleProcessorIndex()
函数ID: N_3094分支数: 24分支覆盖率: 58.33%调用链：
GetRuleProcessorIndex()->
GetMutithreadFrameObj()
函数ID: N_207分支数: 0分支覆盖率: --调用链：
GetMutithreadFrameObj()->
GetCurrectRecordHeader()
函数ID: N_270分支数: 4分支覆盖率: 50.00%调用链：
GetCurrectRecordHeader()->
GetThreadNo()
函数ID: N_203分支数: 0分支覆盖率: --调用链：
GetThreadNo()->
GetMaxRecordThreadCount()
函数ID: N_269分支数: 0分支覆盖率: --调用链：
GetMaxRecordThreadCount()->
ProcessGroupRuleInRF()
函数ID: N_3090分支数: 20分支覆盖率: 65.00%调用链：
ProcessGroupRuleInRF()->RelativeCheck()->RuleProcess()
RelativeCheck()
函数ID: N_3329分支数: 14分支覆盖率: 71.43%调用链：
RelativeCheck()->RuleRelativeCheck()->BusinessRelativeCheck()->BusinessRelativeCheck()->BusinessRelativeCheck()->FactorsRelativeCheck()
RuleRelativeCheck()
函数ID: N_3336分支数: 14分支覆盖率: 50.00%调用链：
RuleRelativeCheck()->ExclusionCheck()->EffectTimeCheck()->EffectTimeRangeCheck()
ExclusionCheck()
函数ID: N_3333分支数: 14分支覆盖率: 35.71%调用链：
ExclusionCheck()->GetCFactorParamTypeBak()
GetCFactorParamTypeBak()
函数ID: N_2165分支数: 2分支覆盖率: 100.00%调用链：
GetCFactorParamTypeBak()->
EffectTimeCheck()
函数ID: N_3348分支数: 10分支覆盖率: 40.00%调用链：
EffectTimeCheck()->
EffectTimeRangeCheck()
函数ID: N_3349分支数: 10分支覆盖率: 10.00%调用链：
EffectTimeRangeCheck()->
BusinessRelativeCheck()
函数ID: N_3310分支数: 2分支覆盖率: 0.00%调用链：
BusinessRelativeCheck()->
BusinessRelativeCheck()
函数ID: N_3548分支数: 8分支覆盖率: 75.00%调用链：
BusinessRelativeCheck()->
BusinessRelativeCheck()
函数ID: N_3557分支数: 8分支覆盖率: 75.00%调用链：
BusinessRelativeCheck()->
FactorsRelativeCheck()
函数ID: N_3337分支数: 10分支覆盖率: 30.00%调用链：
FactorsRelativeCheck()->FactorParamRelativeCheck()
FactorParamRelativeCheck()
函数ID: N_3324分支数: 0分支覆盖率: --调用链：
FactorParamRelativeCheck()->ParamRelativeCheck_Entrance()
ParamRelativeCheck_Entrance()
函数ID: N_3508分支数: 4分支覆盖率: Entrance调用链：
ParamRelativeCheck_Entrance()->ParamRelativeCheck()->ParamRelativeCheck()->ParamRelativeCheck()
ParamRelativeCheck()
函数ID: N_3319分支数: 0分支覆盖率: --调用链：
ParamRelativeCheck()->ControlTypeCheck()->MarketTypeCheck()->ExcludeStockCheck()->DirectionRelativeCheck()->TraderRelativeCheck()
ControlTypeCheck()
函数ID: N_3513分支数: 34分支覆盖率: 44.12%调用链：
ControlTypeCheck()->StockTypeCheck()->StockPoolCheck()->StockDimensionCheck()->StockPoolTypeCheck()
StockTypeCheck()
函数ID: N_3514分支数: 4分支覆盖率: 75.00%调用链：
StockTypeCheck()->
StockPoolCheck()
函数ID: N_3515分支数: 6分支覆盖率: 0.00%调用链：
StockPoolCheck()->
StockDimensionCheck()
函数ID: N_3522分支数: 10分支覆盖率: 60.00%调用链：
StockDimensionCheck()->GetParamValueCount()->GetCStockPool()->IsSecurityUnderControl()
GetParamValueCount()
函数ID: N_336分支数: 0分支覆盖率: --调用链：
GetParamValueCount()->
GetCStockPool()
函数ID: N_1244分支数: 0分支覆盖率: --调用链：
GetCStockPool()->
IsSecurityUnderControl()
函数ID: N_2162分支数: 6分支覆盖率: 33.33%调用链：
IsSecurityUnderControl()->GetCDimStockBak()
GetCDimStockBak()
函数ID: N_2161分支数: 2分支覆盖率: 50.00%调用链：
GetCDimStockBak()->
StockPoolTypeCheck()
函数ID: N_3516分支数: 2分支覆盖率: 0.00%调用链：
StockPoolTypeCheck()->
MarketTypeCheck()
函数ID: N_3521分支数: 10分支覆盖率: 40.00%调用链：
MarketTypeCheck()->
ExcludeStockCheck()
函数ID: N_3520分支数: 4分支覆盖率: 25.00%调用链：
ExcludeStockCheck()->
DirectionRelativeCheck()
函数ID: N_3318分支数: 12分支覆盖率: 0.00%调用链：
DirectionRelativeCheck()->
TraderRelativeCheck()
函数ID: N_3317分支数: 2分支覆盖率: 0.00%调用链：
TraderRelativeCheck()->
ParamRelativeCheck()
函数ID: N_3551分支数: 26分支覆盖率: 57.69%调用链：
ParamRelativeCheck()->ControlTypeCheck()->DirectionRelativeCheck()->ExcludeStockCheck()->MarketTypeCheck()->PriceTypeCheck()->ScientificBoardCheck()
DirectionRelativeCheck()
函数ID: N_3519分支数: 16分支覆盖率: 50.00%调用链：
DirectionRelativeCheck()->
PriceTypeCheck()
函数ID: N_3555分支数: 18分支覆盖率: 38.89%调用链：
PriceTypeCheck()->IsLimitPrice()
IsLimitPrice()
函数ID: N_3553分支数: 12分支覆盖率: 16.67%调用链：
IsLimitPrice()->
ScientificBoardCheck()
函数ID: N_3554分支数: 8分支覆盖率: 37.50%调用链：
ScientificBoardCheck()->
ParamRelativeCheck()
函数ID: N_3561分支数: 16分支覆盖率: 62.50%调用链：
ParamRelativeCheck()->OperationCheck()->ControlTypeCheck()->WhitelistControl()->ExcludeStockCheck()->MarketTypeCheck()
OperationCheck()
函数ID: N_3562分支数: 12分支覆盖率: 58.33%调用链：
OperationCheck()->
WhitelistControl()
函数ID: N_3563分支数: 8分支覆盖率: 12.50%调用链：
WhitelistControl()->
RuleProcess()
函数ID: N_3331分支数: 30分支覆盖率: 23.33%调用链：
RuleProcess()->WarnInfoLanding()->CalcAllFactor()->GetFactorCalcResult()->CheckDenominator()->CalcFormula()->RiskWarnJudge()->PerfStatistic()
WarnInfoLanding()
函数ID: N_3343分支数: 4分支覆盖率: 50.00%调用链：
WarnInfoLanding()->GetNewRecord()->SetLayerInfo()->SetRuleInfo()->SetEntrustInfo()->SetContraOrderInfo()->StatisticForbidWarningInfo()->WarnInfoLanding2Rsp()
GetNewRecord()
函数ID: N_1724分支数: 0分支覆盖率: --调用链：
GetNewRecord()->GetNewRecord()
GetNewRecord()
函数ID: N_2182分支数: 6分支覆盖率: 50.00%调用链：
GetNewRecord()->Lock()->Unlock()
Lock()
函数ID: N_2180分支数: 2分支覆盖率: 50.00%调用链：
Lock()->
Unlock()
函数ID: N_2181分支数: 0分支覆盖率: --调用链：
Unlock()->
SetLayerInfo()
函数ID: N_3346分支数: 30分支覆盖率: 50.00%调用链：
SetLayerInfo()->
SetRuleInfo()
函数ID: N_3345分支数: 16分支覆盖率: 62.50%调用链：
SetRuleInfo()->
SetEntrustInfo()
函数ID: N_3344分支数: 6分支覆盖率: 33.33%调用链：
SetEntrustInfo()->size()->ConvertDouble()
size()
函数ID: N_1151分支数: 0分支覆盖率: --调用链：
size()->
SetContraOrderInfo()
函数ID: N_3350分支数: 28分支覆盖率: 3.57%调用链：
SetContraOrderInfo()->GetParamValueCount()->GetParamValue()->GetCombi()->ConvertDouble()
GetParamValue()
函数ID: N_337分支数: 0分支覆盖率: --调用链：
GetParamValue()->
GetCombi()
函数ID: N_1268分支数: 0分支覆盖率: --调用链：
GetCombi()->
StatisticForbidWarningInfo()
函数ID: N_3351分支数: 2分支覆盖率: 50.00%调用链：
StatisticForbidWarningInfo()->
WarnInfoLanding2Rsp()
函数ID: N_3341分支数: 8分支覆盖率: 50.00%调用链：
WarnInfoLanding2Rsp()->GetRedoRiskCheckWarn()->ConvertDouble()
GetRedoRiskCheckWarn()
函数ID: N_2235分支数: 2分支覆盖率: 50.00%调用链：
GetRedoRiskCheckWarn()->Lock()->Unlock()
Lock()
函数ID: N_360分支数: 0分支覆盖率: --调用链：
Lock()->
Unlock()
函数ID: N_361分支数: 0分支覆盖率: --调用链：
Unlock()->
CalcAllFactor()
函数ID: N_3330分支数: 14分支覆盖率: 28.57%调用链：
CalcAllFactor()->CalcFactor()
CalcFactor()
函数ID: N_3326分支数: 0分支覆盖率: --调用链：
CalcFactor()->Process()
Process()
函数ID: N_3511分支数: 20分支覆盖率: 30.00%调用链：
Process()->CalcFactorValue()->CalcFactorValue()->CalcFactorValue()->CalcFactorValue()->PerfStatistic()
CalcFactorValue()
函数ID: N_3316分支数: 6分支覆盖率: 0.00%调用链：
CalcFactorValue()->CalcByLayer()
CalcByLayer()
函数ID: N_3312分支数: 30分支覆盖率: 0.00%调用链：
CalcByLayer()->
CalcFactorValue()
函数ID: N_3321分支数: 6分支覆盖率: 0.00%调用链：
CalcFactorValue()->
CalcFactorValue()
函数ID: N_3550分支数: 112分支覆盖率: 9.82%调用链：
CalcFactorValue()->IsLimitPrice()
CalcFactorValue()
函数ID: N_3560分支数: 2分支覆盖率: 50.00%调用链：
CalcFactorValue()->
PerfStatistic()
函数ID: N_3512分支数: 4分支覆盖率: 0.00%调用链：
PerfStatistic()->GetThreadNo()->LockFactorPerfFile()->UnLockFactorPerfFile()
LockFactorPerfFile()
函数ID: N_2171分支数: 2分支覆盖率: 0.00%调用链：
LockFactorPerfFile()->
UnLockFactorPerfFile()
函数ID: N_2172分支数: 0分支覆盖率: --调用链：
UnLockFactorPerfFile()->
GetFactorCalcResult()
函数ID: N_3334分支数: 14分支覆盖率: 28.57%调用链：
GetFactorCalcResult()->
CheckDenominator()
函数ID: N_3335分支数: 12分支覆盖率: 8.33%调用链：
CheckDenominator()->WarnInfoLanding()
CalcFormula()
函数ID: N_3347分支数: 18分支覆盖率: 38.89%调用链：
CalcFormula()->
RiskWarnJudge()
函数ID: N_3339分支数: 106分支覆盖率: 18.87%调用链：
RiskWarnJudge()->WarnInfoLanding()
PerfStatistic()
函数ID: N_3332分支数: 4分支覆盖率: 0.00%调用链：
PerfStatistic()->GetThreadNo()
MutexRuleQueue()
函数ID: N_3093分支数: 2分支覆盖率: 0.00%调用链：
MutexRuleQueue()->GetRuleProcessorIndex()
MutexRuleProcessStart()
函数ID: N_3092分支数: 0分支覆盖率: --调用链：
MutexRuleProcessStart()->ProcessGroupRuleInRF()->GetThreadNo()
OrderCheckResult()
函数ID: N_6537分支数: 4分支覆盖率: 75.00%调用链：
OrderCheckResult()->
CheckRisk()
函数ID: N_2838分支数: 6分支覆盖率: 33.33%调用链：
CheckRisk()->GetSecurityInfo()->GetThreadNo()->RiskCheck()
UpdateTempTotalFrozen()
函数ID: N_2857分支数: 10分支覆盖率: 10.00%调用链：
UpdateTempTotalFrozen()->
UpdateTempTotalFrozen()
函数ID: N_1502分支数: 0分支覆盖率: --调用链：
UpdateTempTotalFrozen()->
SetErrorNo()
函数ID: N_1499分支数: 0分支覆盖率: --调用链：
SetErrorNo()->
UpdateBusinData()
函数ID: N_3035分支数: 0分支覆盖率: --调用链：
UpdateBusinData()->UpdateAssetday()->UpdateHoldReal()->InsertEntrust()
UpdateAssetday()
函数ID: N_3048分支数: 0分支覆盖率: --调用链：
UpdateAssetday()->
UpdateHoldReal()
函数ID: N_3049分支数: 8分支覆盖率: 25.00%调用链：
UpdateHoldReal()->UpdateETFHoldReal()->UpdateStockHoldReal()
UpdateETFHoldReal()
函数ID: N_3050分支数: 4分支覆盖率: 50.00%调用链：
UpdateETFHoldReal()->GetHoldRealByCode()->NewStockHoldReal()
NewStockHoldReal()
函数ID: N_1540分支数: 4分支覆盖率: 50.00%调用链：
NewStockHoldReal()->InsertStockHoldReal()
InsertStockHoldReal()
函数ID: N_1603分支数: 2分支覆盖率: 100.00%调用链：
InsertStockHoldReal()->
UpdateStockHoldReal()
函数ID: N_3051分支数: 28分支覆盖率: 0.00%调用链：
UpdateStockHoldReal()->JudgeSZVirtualFundCode()->GetExchangeIndex()->GetHoldRealByCode()->GetStockCode()->NewStockHoldReal()
JudgeSZVirtualFundCode()
函数ID: N_2402分支数: 2分支覆盖率: 0.00%调用链：
JudgeSZVirtualFundCode()->
InsertEntrust()
函数ID: N_3052分支数: 22分支覆盖率: 50.00%调用链：
InsertEntrust()->GetSerialInfo()->GetEntrustSerialNo()->NewEtfStockEntrust()->SetStockEntrustSysNo()->BatchBindEntrust()->itoa()->GetConnectID()->InsertEntrustDeatil()
NewEtfStockEntrust()
函数ID: N_1775分支数: 6分支覆盖率: 50.00%调用链：
NewEtfStockEntrust()->SetStockEntrust()
SetStockEntrust()
函数ID: N_1512分支数: 10分支覆盖率: 20.00%调用链：
SetStockEntrust()->GetRecordCount()
SetStockEntrustSysNo()
函数ID: N_1273分支数: 4分支覆盖率: 0.00%调用链：
SetStockEntrustSysNo()->GetExternSys()->NewExternSys()->SetStockEntrust()
GetExternSys()
函数ID: N_1325分支数: 0分支覆盖率: --调用链：
GetExternSys()->
NewExternSys()
函数ID: N_1324分支数: 0分支覆盖率: --调用链：
NewExternSys()->
SetStockEntrust()
函数ID: N_1634分支数: 2分支覆盖率: 0.00%调用链：
SetStockEntrust()->GetConfig()
GetConfig()
函数ID: N_156分支数: 0分支覆盖率: --调用链：
GetConfig()->
BatchBindEntrust()
函数ID: N_1517分支数: 12分支覆盖率: 25.00%调用链：
BatchBindEntrust()->GetRecordCount()->NewBatchEntrustInfo()->GetBatchEntrustInfo()
NewBatchEntrustInfo()
函数ID: N_1515分支数: 2分支覆盖率: 50.00%调用链：
NewBatchEntrustInfo()->
GetBatchEntrustInfo()
函数ID: N_1516分支数: 2分支覆盖率: 50.00%调用链：
GetBatchEntrustInfo()->
GetConnectID()
函数ID: N_198分支数: 0分支覆盖率: --调用链：
GetConnectID()->
InsertEntrustDeatil()
函数ID: N_3053分支数: 38分支覆盖率: 21.05%调用链：
InsertEntrustDeatil()->JudgeSZVirtualFundCode()->NewEntrustDetail()->GetStockCode()->itoa()->GetExchangeIndex()
NewEntrustDetail()
函数ID: N_1612分支数: 2分支覆盖率: 50.00%调用链：
NewEntrustDetail()->
UpdateBusinData()
函数ID: N_2839分支数: 4分支覆盖率: 50.00%调用链：
UpdateBusinData()->GetThreadNo()->UpdateAssetday()->UpdateHoldReal()->UpdateInstanceHold()->InsertEntrust()
UpdateAssetday()
函数ID: N_2842分支数: 0分支覆盖率: --调用链：
UpdateAssetday()->UpdateCashEnableValue()
UpdateCashEnableValue()
函数ID: N_57分支数: 8分支覆盖率: 62.50%调用链：
UpdateCashEnableValue()->GetCashEnableFormulaHashKey()->GetCashEnableCfgFieldByKey()->GetNextNTradeDay()->GetCashEnableFactorField()
UpdateHoldReal()
函数ID: N_2843分支数: 2分支覆盖率: 50.00%调用链：
UpdateHoldReal()->GetHoldRealByCode()->NewStockHoldReal()->GetThreadNo()
UpdateInstanceHold()
函数ID: N_2844分支数: 2分支覆盖率: 0.00%调用链：
UpdateInstanceHold()->GetInstanceHoldByCode()->NewInstanceHold()->GetThreadNo()->GetStockCode()
InsertEntrust()
函数ID: N_2845分支数: 22分支覆盖率: 50.00%调用链：
InsertEntrust()->GetThreadNo()->GetSerialInfo()->GetSysParamVal()->GetEntrustSerialNo()->NewStockEntrust()->BatchBindEntrust()
NewStockEntrust()
函数ID: N_1774分支数: 6分支覆盖率: 50.00%调用链：
NewStockEntrust()->SetStockEntrust()
OfferOrder()
函数ID: N_3039分支数: 4分支覆盖率: 25.00%调用链：
OfferOrder()->InnerMarketOfferOrder()->OutMarketOfferOrder()
InnerMarketOfferOrder()
函数ID: N_3040分支数: 22分支覆盖率: 27.27%调用链：
InnerMarketOfferOrder()->ConvertDouble()->GetTransParam()
GetTransParam()
函数ID: N_296分支数: 6分支覆盖率: 83.33%调用链：
GetTransParam()->
OutMarketOfferOrder()
函数ID: N_3041分支数: 0分支覆盖率: --调用链：
OutMarketOfferOrder()->
OfferOrder()
函数ID: N_2841分支数: 0分支覆盖率: --调用链：
OfferOrder()->OfferStockOrder()
OfferStockOrder()
函数ID: N_64分支数: 8分支覆盖率: 25.00%调用链：
OfferStockOrder()->GetThreadNo()->ConvertDouble()->itoa()->GetSeat()->GetTransParam()
GetSeat()
函数ID: N_1282分支数: 0分支覆盖率: --调用链：
GetSeat()->
WriteBusinToDBRedo()
函数ID: N_3042分支数: 36分支覆盖率: 27.78%调用链：
WriteBusinToDBRedo()->TagTodb()->GetHead()->ConvertDouble()->itoa()->GetEntrustDetailCount()->GetEntrustDetail()->GetExchangeType()
TagTodb()
函数ID: N_1431分支数: 0分支覆盖率: --调用链：
TagTodb()->
GetHead()
函数ID: N_1386分支数: 0分支覆盖率: --调用链：
GetHead()->
GetEntrustDetailCount()
函数ID: N_1613分支数: 0分支覆盖率: --调用链：
GetEntrustDetailCount()->GetRecordCount()
GetEntrustDetail()
函数ID: N_1614分支数: 6分支覆盖率: 50.00%调用链：
GetEntrustDetail()->GetRecordCount()
GetExchangeType()
函数ID: N_9分支数: 24分支覆盖率: 58.33%调用链：
GetExchangeType()->
WriteBusinToDBRedo()
函数ID: N_2851分支数: 2分支覆盖率: 50.00%调用链：
WriteBusinToDBRedo()->GetCutBackSysType()
GetCutBackSysType()
函数ID: N_167分支数: 0分支覆盖率: --调用链：
GetCutBackSysType()->
WriteSyncRedo()
函数ID: N_3055分支数: 2分支覆盖率: 50.00%调用链：
WriteSyncRedo()->GetEntrustDetailCount()
WriteSyncRedo()
函数ID: N_2847分支数: 26分支覆盖率: 38.46%调用链：
WriteSyncRedo()->GetOrginEntrustByNo()->GetHoldFactorCount()->GetHoldFactorCount()->GetCashEnableFactorCount()->GetSysParamVal()->IsEntrustDone()->GetSerialInfo()
GetOrginEntrustByNo()
函数ID: N_28分支数: 0分支覆盖率: --调用链：
GetOrginEntrustByNo()->GetStockEntrust()->GetSerialInfo()
GetStockEntrust()
函数ID: N_1511分支数: 2分支覆盖率: 50.00%调用链：
GetStockEntrust()->GetRecordCount()
GetHoldFactorCount()
函数ID: N_1581分支数: 0分支覆盖率: --调用链：
GetHoldFactorCount()->GetRecordCount()
GetHoldFactorCount()
函数ID: N_1557分支数: 0分支覆盖率: --调用链：
GetHoldFactorCount()->GetRecordCount()
GetCashEnableFactorCount()
函数ID: N_1534分支数: 0分支覆盖率: --调用链：
GetCashEnableFactorCount()->GetRecordCount()
IsEntrustDone()
函数ID: N_1524分支数: 2分支覆盖率: 0.00%调用链：
IsEntrustDone()->GetRecordCount()
RollBackRiskData()
函数ID: N_3047分支数: 6分支覆盖率: 0.00%调用链：
RollBackRiskData()->RollBackBusinData()->RiskETFOrderUpdate()
RollBackBusinData()
函数ID: N_3043分支数: 10分支覆盖率: 0.00%调用链：
RollBackBusinData()->UpdateCashEnableValue()
RollBackRiskData()
函数ID: N_2840分支数: 6分支覆盖率: 0.00%调用链：
RollBackRiskData()->Remove()->GetSecurityInfo()->GetPreSumFlag()->RiskOrderUpdate()
Remove()
函数ID: N_2605分支数: 28分支覆盖率: 21.43%调用链：
Remove()->Lock()->Unlock()
SetResponse()
函数ID: N_3045分支数: 2分支覆盖率: 100.00%调用链：
SetResponse()->itoa()
SetResponse()
函数ID: N_2854分支数: 4分支覆盖率: 50.00%调用链：
SetResponse()->itoa()->GetExchangeType()->ConvertDouble()
总分支数：2048
已覆盖分支数：674