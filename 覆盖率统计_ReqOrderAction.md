<h2 id="reqorderaction">ReqOrderAction()</h2>
<p>函数ID: N_2287<br>分支数: 14<br>分支覆盖率: 71.43%<br>调用链：
ReqOrderAction()-&gt;GetThreadNo()-&gt;Rewind()-&gt;GetOrginEntrustByRefer()-&gt;GetOrginEntrustByNo()-&gt;GetSerialInfo()-&gt;GetBatchEntrustInfo()-&gt;Init()-&gt;DoProcess()-&gt;CommitProcess()-&gt;StockActionSetEntrustDone()-&gt;Response()-&gt;Run()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2287.png#pic_left" /></p>
<h2 id="getthreadno">GetThreadNo()</h2>
<p>函数ID: N_168<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetThreadNo()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/168.png#pic_left" /></p>
<h2 id="rewind">Rewind()</h2>
<p>函数ID: N_1500<br>分支数: 0<br>分支覆盖率: --<br>调用链：
Rewind()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1500.png#pic_left" /></p>
<h2 id="getorginentrustbyrefer">GetOrginEntrustByRefer()</h2>
<p>函数ID: N_37<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetOrginEntrustByRefer()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/37.png#pic_left" /></p>
<h2 id="getorginentrustbyno">GetOrginEntrustByNo()</h2>
<p>函数ID: N_28<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetOrginEntrustByNo()-&gt;GetStockEntrust()-&gt;GetSerialInfo()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/28.png#pic_left" /></p>
<h2 id="getstockentrust">GetStockEntrust()</h2>
<p>函数ID: N_1054<br>分支数: 2<br>分支覆盖率: 100.00%<br>调用链：
GetStockEntrust()-&gt;GetRecordCount()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1054.png#pic_left" /></p>
<h2 id="getrecordcount">GetRecordCount()</h2>
<p>函数ID: N_381<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetRecordCount()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/381.png#pic_left" /></p>
<h2 id="getserialinfo">GetSerialInfo()</h2>
<p>函数ID: N_1435<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetSerialInfo()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1435.png#pic_left" /></p>
<h2 id="getbatchentrustinfo">GetBatchEntrustInfo()</h2>
<p>函数ID: N_1059<br>分支数: 2<br>分支覆盖率: 100.00%<br>调用链：
GetBatchEntrustInfo()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1059.png#pic_left" /></p>
<h2 id="init">Init()</h2>
<p>函数ID: N_2730<br>分支数: 16<br>分支覆盖率: 87.50%<br>调用链：
Init()-&gt;GetHead()-&gt;GetGlobalData()-&gt;GetOptionalReader()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2730.png#pic_left" /></p>
<h2 id="gethead">GetHead()</h2>
<p>函数ID: N_1499<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetHead()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1499.png#pic_left" /></p>
<h2 id="getglobaldata">GetGlobalData()</h2>
<p>函数ID: N_164<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetGlobalData()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/164.png#pic_left" /></p>
<h2 id="getoptionalreader">GetOptionalReader()</h2>
<p>函数ID: N_1501<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetOptionalReader()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1501.png#pic_left" /></p>
<h2 id="doprocess">DoProcess()</h2>
<p>函数ID: N_2727<br>分支数: 12<br>分支覆盖率: 66.67%<br>调用链：
DoProcess()-&gt;CheckSystemStatus()-&gt;GetEntrust()-&gt;Lock()-&gt;UnLock()-&gt;GetSysParamVal()-&gt;SendToUnionRiskAction()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2727.png#pic_left" /></p>
<h2 id="checksystemstatus">CheckSystemStatus()</h2>
<p>函数ID: N_2733<br>分支数: 0<br>分支覆盖率: --<br>调用链：
CheckSystemStatus()-&gt;CheckArbState()-&gt;CheckSysState()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2733.png#pic_left" /></p>
<h2 id="checkarbstate">CheckArbState()</h2>
<p>函数ID: N_3<br>分支数: 2<br>分支覆盖率: 100.00%<br>调用链：
CheckArbState()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/3.png#pic_left" /></p>
<h2 id="checksysstate">CheckSysState()</h2>
<p>函数ID: N_4<br>分支数: 2<br>分支覆盖率: 50.00%<br>调用链：
CheckSysState()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/4.png#pic_left" /></p>
<h2 id="getentrust">GetEntrust()</h2>
<p>函数ID: N_2734<br>分支数: 18<br>分支覆盖率: 33.33%<br>调用链：
GetEntrust()-&gt;GetOrginEntrustByRefer()-&gt;GetOrginEntrustByNo()-&gt;GetSerialInfo()-&gt;GetBatchEntrustInfo()-&gt;GetStockEntrust()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2734.png#pic_left" /></p>
<h2 id="getstockentrust_1">GetStockEntrust()</h2>
<p>函数ID: N_1772<br>分支数: 2<br>分支覆盖率: 0.00%<br>调用链：
GetStockEntrust()-&gt;GetRecordCount()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1772.png#pic_left" /></p>
<h2 id="lock">Lock()</h2>
<p>函数ID: N_247<br>分支数: 2<br>分支覆盖率: 0.00%<br>调用链：
Lock()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/247.png#pic_left" /></p>
<h2 id="unlock">UnLock()</h2>
<p>函数ID: N_248<br>分支数: 0<br>分支覆盖率: --<br>调用链：
UnLock()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/248.png#pic_left" /></p>
<h2 id="getsysparamval">GetSysParamVal()</h2>
<p>函数ID: N_1469<br>分支数: 2<br>分支覆盖率: 50.00%<br>调用链：
GetSysParamVal()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1469.png#pic_left" /></p>
<h2 id="sendtounionriskaction">SendToUnionRiskAction()</h2>
<p>函数ID: N_2760<br>分支数: 10<br>分支覆盖率: 0.00%<br>调用链：
SendToUnionRiskAction()-&gt;GetSerialInfo()-&gt;GetEntrustSerialNo()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2760.png#pic_left" /></p>
<h2 id="getentrustserialno">GetEntrustSerialNo()</h2>
<p>函数ID: N_1050<br>分支数: 2<br>分支覆盖率: 50.00%<br>调用链：
GetEntrustSerialNo()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1050.png#pic_left" /></p>
<h2 id="commitprocess">CommitProcess()</h2>
<p>函数ID: N_2728<br>分支数: 40<br>分支覆盖率: 37.50%<br>调用链：
CommitProcess()-&gt;GetSecurityInfo()-&gt;GetOrginEntrustByNo()-&gt;AddEtfOrderCashInfo()-&gt;GetSysParamVal()-&gt;ToUnionRisk()-&gt;getLdpContext()-&gt;WriteSyncRedo()-&gt;WriteToDBRedo()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2728.png#pic_left" /></p>
<h2 id="getsecurityinfo">GetSecurityInfo()</h2>
<p>函数ID: N_1132<br>分支数: 2<br>分支覆盖率: 100.00%<br>调用链：
GetSecurityInfo()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1132.png#pic_left" /></p>
<h2 id="addetfordercashinfo">AddEtfOrderCashInfo()</h2>
<p>函数ID: N_3548<br>分支数: 0<br>分支覆盖率: --<br>调用链：
AddEtfOrderCashInfo()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/3548.png#pic_left" /></p>
<h2 id="tounionrisk">ToUnionRisk()</h2>
<p>函数ID: N_2738<br>分支数: 0<br>分支覆盖率: --<br>调用链：
ToUnionRisk()-&gt;SendToUnionRiskWithcfm()-&gt;GetStockPushCount()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2738.png#pic_left" /></p>
<h2 id="sendtounionriskwithcfm">SendToUnionRiskWithcfm()</h2>
<p>函数ID: N_61<br>分支数: 2<br>分支覆盖率: 0.00%<br>调用链：
SendToUnionRiskWithcfm()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/61.png#pic_left" /></p>
<h2 id="getstockpushcount">GetStockPushCount()</h2>
<p>函数ID: N_1780<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetStockPushCount()-&gt;GetRecordCount()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1780.png#pic_left" /></p>
<h2 id="getldpcontext">getLdpContext()</h2>
<p>函数ID: N_175<br>分支数: 0<br>分支覆盖率: --<br>调用链：
getLdpContext()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/175.png#pic_left" /></p>
<h2 id="writesyncredo">WriteSyncRedo()</h2>
<p>函数ID: N_2746<br>分支数: 14<br>分支覆盖率: 64.29%<br>调用链：
WriteSyncRedo()-&gt;GetHoldFactorCount()-&gt;GetHoldFactorCount()-&gt;GetCashEnableFactorCount()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2746.png#pic_left" /></p>
<h2 id="getholdfactorcount">GetHoldFactorCount()</h2>
<p>函数ID: N_1124<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetHoldFactorCount()-&gt;GetRecordCount()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1124.png#pic_left" /></p>
<h2 id="getholdfactorcount_1">GetHoldFactorCount()</h2>
<p>函数ID: N_1100<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetHoldFactorCount()-&gt;GetRecordCount()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1100.png#pic_left" /></p>
<h2 id="getcashenablefactorcount">GetCashEnableFactorCount()</h2>
<p>函数ID: N_1077<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetCashEnableFactorCount()-&gt;GetRecordCount()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1077.png#pic_left" /></p>
<h2 id="writetodbredo">WriteToDBRedo()</h2>
<p>函数ID: N_2757<br>分支数: 10<br>分支覆盖率: 50.00%<br>调用链：
WriteToDBRedo()-&gt;GetCutBackSysType()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2757.png#pic_left" /></p>
<h2 id="getcutbacksystype">GetCutBackSysType()</h2>
<p>函数ID: N_132<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetCutBackSysType()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/132.png#pic_left" /></p>
<h2 id="stockactionsetentrustdone">StockActionSetEntrustDone()</h2>
<p>函数ID: N_2276<br>分支数: 4<br>分支覆盖率: 25.00%<br>调用链：
StockActionSetEntrustDone()-&gt;GetSysParamVal()-&gt;SetEntrustDone()-&gt;GetSerialInfo()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2276.png#pic_left" /></p>
<h2 id="setentrustdone">SetEntrustDone()</h2>
<p>函数ID: N_1066<br>分支数: 2<br>分支覆盖率: 50.00%<br>调用链：
SetEntrustDone()-&gt;GetRecordCount()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1066.png#pic_left" /></p>
<h2 id="response">Response()</h2>
<p>函数ID: N_2744<br>分支数: 10<br>分支覆盖率: 80.00%<br>调用链：
Response()-&gt;Done()-&gt;itoa()-&gt;GetOptionalWriter()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2744.png#pic_left" /></p>
<h2 id="done">Done()</h2>
<p>函数ID: N_1551<br>分支数: 4<br>分支覆盖率: 100.00%<br>调用链：
Done()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1551.png#pic_left" /></p>
<h2 id="itoa">itoa()</h2>
<p>函数ID: N_6467<br>分支数: 10<br>分支覆盖率: 0.00%<br>调用链：
itoa()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/6467.png#pic_left" /></p>
<h2 id="getoptionalwriter">GetOptionalWriter()</h2>
<p>函数ID: N_1550<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetOptionalWriter()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1550.png#pic_left" /></p>
<h2 id="run">Run()</h2>
<p>函数ID: N_2675<br>分支数: 4<br>分支覆盖率: 0.00%<br>调用链：
Run()-&gt;Init()-&gt;GetEntrust()-&gt;CheckActionValid()-&gt;DistinguishBusin()-&gt;GetBasicData()-&gt;CalcBusinData()-&gt;UpdateBusinData()-&gt;UpdateRiskData()-&gt;OfferOrder()-&gt;PushMsg()-&gt;WriteSyncRedo()-&gt;WriteToDBRedo()-&gt;SetResponse()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2675.png#pic_left" /></p>
<h2 id="init_1">Init()</h2>
<p>函数ID: N_2676<br>分支数: 18<br>分支覆盖率: 0.00%<br>调用链：
Init()-&gt;GetHead()-&gt;GetGlobalData()-&gt;GetOptionalReader()-&gt;GetSerialInfo()-&gt;GetEntrustSerialNo()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2676.png#pic_left" /></p>
<h2 id="getentrust_1">GetEntrust()</h2>
<p>函数ID: N_2695<br>分支数: 12<br>分支覆盖率: 0.00%<br>调用链：
GetEntrust()-&gt;GetOrginEntrustByRefer()-&gt;GetOrginEntrustByNo()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2695.png#pic_left" /></p>
<h2 id="checkactionvalid">CheckActionValid()</h2>
<p>函数ID: N_2696<br>分支数: 0<br>分支覆盖率: --<br>调用链：
CheckActionValid()-&gt;CheckOrderActionEntrustStatus()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2696.png#pic_left" /></p>
<h2 id="checkorderactionentruststatus">CheckOrderActionEntrustStatus()</h2>
<p>函数ID: N_38<br>分支数: 2<br>分支覆盖率: 100.00%<br>调用链：
CheckOrderActionEntrustStatus()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/38.png#pic_left" /></p>
<h2 id="distinguishbusin">DistinguishBusin()</h2>
<p>函数ID: N_2677<br>分支数: 4<br>分支覆盖率: 0.00%<br>调用链：
DistinguishBusin()-&gt;GetSysParamVal()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2677.png#pic_left" /></p>
<h2 id="getsysparamval_1">GetSysParamVal()</h2>
<p>函数ID: N_1466<br>分支数: 2<br>分支覆盖率: 50.00%<br>调用链：
GetSysParamVal()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1466.png#pic_left" /></p>
<h2 id="getbasicdata">GetBasicData()</h2>
<p>函数ID: N_2678<br>分支数: 6<br>分支覆盖率: 0.00%<br>调用链：
GetBasicData()-&gt;GetSeat()-&gt;GetTrader()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2678.png#pic_left" /></p>
<h2 id="getseat">GetSeat()</h2>
<p>函数ID: N_1445<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetSeat()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1445.png#pic_left" /></p>
<h2 id="gettrader">GetTrader()</h2>
<p>函数ID: N_1415<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetTrader()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1415.png#pic_left" /></p>
<h2 id="calcbusindata">CalcBusinData()</h2>
<p>函数ID: N_2690<br>分支数: 0<br>分支覆盖率: --<br>调用链：
CalcBusinData()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2690.png#pic_left" /></p>
<h2 id="updatebusindata">UpdateBusinData()</h2>
<p>函数ID: N_2691<br>分支数: 2<br>分支覆盖率: 0.00%<br>调用链：
UpdateBusinData()-&gt;InsertCancelEntrust()-&gt;UpdateBusinessDataOfInner()-&gt;UpdateBusinessDataOfOut()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2691.png#pic_left" /></p>
<h2 id="insertcancelentrust">InsertCancelEntrust()</h2>
<p>函数ID: N_2698<br>分支数: 4<br>分支覆盖率: 0.00%<br>调用链：
InsertCancelEntrust()-&gt;GetSerialInfo()-&gt;NewEtfStockEntrust()-&gt;GetConnectID()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2698.png#pic_left" /></p>
<h2 id="newetfstockentrust">NewEtfStockEntrust()</h2>
<p>函数ID: N_1771<br>分支数: 6<br>分支覆盖率: 50.00%<br>调用链：
NewEtfStockEntrust()-&gt;SetStockEntrust()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1771.png#pic_left" /></p>
<h2 id="setstockentrust">SetStockEntrust()</h2>
<p>函数ID: N_1055<br>分支数: 10<br>分支覆盖率: 70.00%<br>调用链：
SetStockEntrust()-&gt;GetRecordCount()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1055.png#pic_left" /></p>
<h2 id="getconnectid">GetConnectID()</h2>
<p>函数ID: N_163<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetConnectID()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/163.png#pic_left" /></p>
<h2 id="updatebusinessdataofinner">UpdateBusinessDataOfInner()</h2>
<p>函数ID: N_2699<br>分支数: 0<br>分支覆盖率: --<br>调用链：
UpdateBusinessDataOfInner()-&gt;UpdateAssetday()-&gt;UpdateOrginEntrust()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2699.png#pic_left" /></p>
<h2 id="updateassetday">UpdateAssetday()</h2>
<p>函数ID: N_2703<br>分支数: 0<br>分支覆盖率: --<br>调用链：
UpdateAssetday()-&gt;UpdateCashEnableValue()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2703.png#pic_left" /></p>
<h2 id="updatecashenablevalue">UpdateCashEnableValue()</h2>
<p>函数ID: N_57<br>分支数: 8<br>分支覆盖率: 62.50%<br>调用链：
UpdateCashEnableValue()-&gt;GetCashEnableFormulaHashKey()-&gt;GetCashEnableCfgFieldByKey()-&gt;GetNextNTradeDay()-&gt;GetCashEnableFactorField()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/57.png#pic_left" /></p>
<h2 id="getcashenableformulahashkey">GetCashEnableFormulaHashKey()</h2>
<p>函数ID: N_53<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetCashEnableFormulaHashKey()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/53.png#pic_left" /></p>
<h2 id="getcashenablecfgfieldbykey">GetCashEnableCfgFieldByKey()</h2>
<p>函数ID: N_1727<br>分支数: 2<br>分支覆盖率: 50.00%<br>调用链：
GetCashEnableCfgFieldByKey()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1727.png#pic_left" /></p>
<h2 id="getnextntradeday">GetNextNTradeDay()</h2>
<p>函数ID: N_1735<br>分支数: 12<br>分支覆盖率: 91.67%<br>调用链：
GetNextNTradeDay()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1735.png#pic_left" /></p>
<h2 id="getcashenablefactorfield">GetCashEnableFactorField()</h2>
<p>函数ID: N_1076<br>分支数: 2<br>分支覆盖率: 100.00%<br>调用链：
GetCashEnableFactorField()-&gt;NewCashEnableFactorField()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1076.png#pic_left" /></p>
<h2 id="newcashenablefactorfield">NewCashEnableFactorField()</h2>
<p>函数ID: N_1080<br>分支数: 2<br>分支覆盖率: 50.00%<br>调用链：
NewCashEnableFactorField()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1080.png#pic_left" /></p>
<h2 id="updateorginentrust">UpdateOrginEntrust()</h2>
<p>函数ID: N_2705<br>分支数: 0<br>分支覆盖率: --<br>调用链：
UpdateOrginEntrust()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2705.png#pic_left" /></p>
<h2 id="updatebusinessdataofout">UpdateBusinessDataOfOut()</h2>
<p>函数ID: N_2700<br>分支数: 6<br>分支覆盖率: 0.00%<br>调用链：
UpdateBusinessDataOfOut()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2700.png#pic_left" /></p>
<h2 id="updateriskdata">UpdateRiskData()</h2>
<p>函数ID: N_2692<br>分支数: 0<br>分支覆盖率: --<br>调用链：
UpdateRiskData()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2692.png#pic_left" /></p>
<h2 id="offerorder">OfferOrder()</h2>
<p>函数ID: N_2679<br>分支数: 8<br>分支覆盖率: 0.00%<br>调用链：
OfferOrder()-&gt;GetTransParam()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2679.png#pic_left" /></p>
<h2 id="gettransparam">GetTransParam()</h2>
<p>函数ID: N_236<br>分支数: 6<br>分支覆盖率: 66.67%<br>调用链：
GetTransParam()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/236.png#pic_left" /></p>
<h2 id="pushmsg">PushMsg()</h2>
<p>函数ID: N_2697<br>分支数: 0<br>分支覆盖率: --<br>调用链：
PushMsg()-&gt;NewPushRecord()-&gt;PushOrder()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2697.png#pic_left" /></p>
<h2 id="newpushrecord">NewPushRecord()</h2>
<p>函数ID: N_2701<br>分支数: 2<br>分支覆盖率: 0.00%<br>调用链：
NewPushRecord()-&gt;NewStockEtfPushRecord()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2701.png#pic_left" /></p>
<h2 id="newstocketfpushrecord">NewStockEtfPushRecord()</h2>
<p>函数ID: N_47<br>分支数: 6<br>分支覆盖率: 0.00%<br>调用链：
NewStockEtfPushRecord()-&gt;NewStockPush()-&gt;NewPushAtAllDim()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/47.png#pic_left" /></p>
<h2 id="newstockpush">NewStockPush()</h2>
<p>函数ID: N_1778<br>分支数: 2<br>分支覆盖率: 50.00%<br>调用链：
NewStockPush()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1778.png#pic_left" /></p>
<h2 id="newpushatalldim">NewPushAtAllDim()</h2>
<p>函数ID: N_44<br>分支数: 8<br>分支覆盖率: 37.50%<br>调用链：
NewPushAtAllDim()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/44.png#pic_left" /></p>
<h2 id="pushorder">PushOrder()</h2>
<p>函数ID: N_2702<br>分支数: 0<br>分支覆盖率: --<br>调用链：
PushOrder()-&gt;PushEtfMsg()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2702.png#pic_left" /></p>
<h2 id="pushetfmsg">PushEtfMsg()</h2>
<p>函数ID: N_49<br>分支数: 8<br>分支覆盖率: 0.00%<br>调用链：
PushEtfMsg()-&gt;GetHead()-&gt;SetRequest()-&gt;GetExchangeType()-&gt;itoa()-&gt;ConvertDouble()-&gt;GetOptionalWriter()-&gt;Push()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/49.png#pic_left" /></p>
<h2 id="gethead_1">GetHead()</h2>
<p>函数ID: N_1549<br>分支数: 0<br>分支覆盖率: --<br>调用链：
GetHead()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1549.png#pic_left" /></p>
<h2 id="setrequest">SetRequest()</h2>
<p>函数ID: N_98<br>分支数: 0<br>分支覆盖率: --<br>调用链：
SetRequest()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/98.png#pic_left" /></p>
<h2 id="getexchangetype">GetExchangeType()</h2>
<p>函数ID: N_9<br>分支数: 24<br>分支覆盖率: 58.33%<br>调用链：
GetExchangeType()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/9.png#pic_left" /></p>
<h2 id="convertdouble">ConvertDouble()</h2>
<p>函数ID: N_214<br>分支数: 0<br>分支覆盖率: --<br>调用链：
ConvertDouble()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/214.png#pic_left" /></p>
<h2 id="push">Push()</h2>
<p>函数ID: N_1553<br>分支数: 0<br>分支覆盖率: --<br>调用链：
Push()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/1553.png#pic_left" /></p>
<h2 id="writesyncredo_1">WriteSyncRedo()</h2>
<p>函数ID: N_2682<br>分支数: 0<br>分支覆盖率: --<br>调用链：
WriteSyncRedo()-&gt;WriteSuccessSyncRedo()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2682.png#pic_left" /></p>
<h2 id="writesuccesssyncredo">WriteSuccessSyncRedo()</h2>
<p>函数ID: N_2683<br>分支数: 6<br>分支覆盖率: 0.00%<br>调用链：
WriteSuccessSyncRedo()-&gt;GetCashEnableFactorCount()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2683.png#pic_left" /></p>
<h2 id="writetodbredo_1">WriteToDBRedo()</h2>
<p>函数ID: N_2687<br>分支数: 2<br>分支覆盖率: 0.00%<br>调用链：
WriteToDBRedo()-&gt;<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2687.png#pic_left" /></p>
<h2 id="setresponse">SetResponse()</h2>
<p>函数ID: N_2680<br>分支数: 6<br>分支覆盖率: 0.00%<br>调用链：
SetResponse()-&gt;Done()-&gt;itoa()-&gt;GetOptionalWriter()<br><img alt="Alt Text" src="https://cdn.jsdelivr.net/gh/Brook108/mdimg1@main/img/2680.png#pic_left" /></p>
<h2 id="364">总分支数：364</h2>
<h2 id="147">已覆盖分支数：147</h2>
