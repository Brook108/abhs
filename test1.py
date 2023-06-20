import networkx as nx
import matplotlib.pyplot as plt

call_graph = nx.DiGraph()

call_graph.add_edges_from([
        ("ReqOrderInsert_--", "Run_62.50%"),
        ("Run_62.50%", "SetOrderIndex_--"),
        ("Run_62.50%", "DistinguishBusin_--"),
        ("Run_62.50%", "DistinguishBusin_--"),
        ("Run_62.50%", "GetBasicData_50.00%"),
        ("Run_62.50%", "GetBasicData_--"),
        ("Run_62.50%", "SendToUnionRisk_0.00%"),
        ("Run_62.50%", "SendToUnionRisk_--"),
        ("Run_62.50%", "CheckBusiness_--"),
        ("Run_62.50%", "CheckBusiness_75.00%"),
        ("Run_62.50%", "CalcBusinData_--"),
        ("Run_62.50%", "CalcBusinData_100.00%"),
        ("Run_62.50%", "GetEntrustBalance_--"),
        ("Run_62.50%", "GetEntrustBalance_--"),
        ("Run_62.50%", "InsertRiskEntrust_50.00%"),
        ("Run_62.50%", "InsertRiskEntrust_16.67%"),
        ("Run_62.50%", "UpdateRiskData_--"),
        ("Run_62.50%", "UpdateRiskData_--"),
        ("Run_62.50%", "CheckEnable_--"),
        ("Run_62.50%", "CheckEnable_83.33%"),
        ("Run_62.50%", "CheckRisk_--"),
        ("Run_62.50%", "CheckRisk_66.67%"),
        ("Run_62.50%", "UpdateTempTotalFrozen_80.00%"),
        ("Run_62.50%", "UpdateTempTotalFrozen_--"),
        ("Run_62.50%", "SetErrorNo_--"),
        ("Run_62.50%", "UpdateBusinData_--"),
        ("Run_62.50%", "UpdateBusinData_100.00%"),
        ("Run_62.50%", "OfferOrder_25.00%"),
        ("Run_62.50%", "OfferOrder_--"),
        ("Run_62.50%", "WriteBusinToDBRedo_41.67%"),
        ("Run_62.50%", "WriteBusinToDBRedo_50.00%"),
        ("Run_62.50%", "WriteSyncRedo_50.00%"),
        ("Run_62.50%", "WriteSyncRedo_61.54%"),
        ("Run_62.50%", "RollBackRiskData_0.00%"),
        ("Run_62.50%", "RollBackRiskData_70.00%"),
        ("Run_62.50%", "SetResponse_100.00%"),
        ("Run_62.50%", "SetResponse_50.00%"),
        ("GetBasicData_50.00%", "GetEtfBasicInfoByEtfCode_100.00%"),
        ("GetBasicData_50.00%", "GetHoldRealByCode_100.00%"),
        ("GetBasicData_50.00%", "GetInstanceHold_0.00%"),
        ("GetBasicData_50.00%", "GetStockCode_100.00%"),
        ("SendToUnionRisk_0.00%", "GetSerialInfo_--"),
        ("SendToUnionRisk_0.00%", "GetEntrustSerialNo_50.00%"),
        ("SendToUnionRisk_0.00%", "GetSeatByIndex_50.00%"),
        ("SendToUnionRisk_0.00%", "ConvertDouble_--")
])

layout = nx.spring_layout(call_graph)
nx.draw(call_graph, pos=layout, with_labels=True, arrows=True)
plt.show()
