import json

import requests


def test():
    data = {"Company": {"Code": "02", "Name": "\u4e0a\u6d77\u5e02", "Description": "string"},
            "BagNo": "YWCN20200925020039", "SendDate": "2020-09-25T10:28:26.000Z", "ProductId": "string",
            "SortCode": "01", "TransportCity": "string", "Memo": "string", "ServiceCode": "2190690",
            "ServiceName": "string", "SupplierCode": "275514769", "SupplierName": "string",
            "MasterId": "cb149da6-fed6-11ea-ae9d-104a7d0758aa", "WaybillNumber": "EB728896224CN",
            "ExchangeNumber": "string", "NumberType": "waybill", "IsSort": 0, "Weight": 0,
            "PrintSortingCode": "01-275514769-2190690-MIX", "TotalWeight": 0, "TotalPiece": 0, "SortingRule": "MIX",
            "CreateId": "2417", "LimitPiece": 99999999, "MinPackageWeight": 0, "MaxPackageWeight": 99999999,
            "English2Bit": "US", "RegionId": 115, "IsVerifyExpressStop": True, "SourceId": 6, "OutWarehouse": "01",
            "MailBoxItem": "N", "PackageRuleCode": "ZF20200910235237", "PackageRuleName": "string",
            "Destination": "200071", "PackingMaterialsRuleCode": 2, "PackingMaterialsRuleName": "string",
            "PackingMaterialsWeight": 0, "IsChangePackage": False, "PackagingRequirement": "string",
            "IsVerifyExchange": False}
    dto = data['NumberType'] = 'waybill'

    # print(json.dumps(data))
    res = requests.get('http://127.0.0.1:5000', json={'NumberType': 'waybill'})
    print(res.json())
