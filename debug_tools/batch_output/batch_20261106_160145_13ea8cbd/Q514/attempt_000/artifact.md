```cardspec
{
  "title": "耳机电量",
  "description": "耳机状态速览",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetEarphoneInfo",
      "arguments": {},
      "writeResultTo": "/data/earphone"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["first","second"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":8,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"first","component":"Column","children":["first_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","height":63,"backgroundColor":"#CCFFFFFF","layoutWeight":1}},{"id":"first_text","component":"Column","children":["first_primary","first_secondary"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"center","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"first_primary","component":"Text","content":"{{ ${/data/earphone/batteryLevel} + '%' }}","styles":{"height":22,"fontSize":16,"fontWeight":700,"maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"first_secondary","component":"Text","content":"{{ '耳机盒 ' + ${/data/earphone/chargingStatusDesc} }}","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#FF1F4799"}},{"id":"second","component":"Column","children":["second_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","height":63,"backgroundColor":"#CCFFFFFF","layoutWeight":1}},{"id":"second_text","component":"Column","children":["second_primary","second_secondary"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"center","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"second_primary","component":"Text","content":"{{ '左耳 ' + ${/data/earphone/leftBatteryLevel} + '%' }}","styles":{"height":22,"fontSize":16,"fontWeight":700,"maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"second_secondary","component":"Text","content":"{{ '左耳 ' + ${/data/earphone/leftChargingStatusDesc} }}","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#FF1F4799"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"earphone":{"batteryLevel":80,"chargingStatusDesc":"未充电","leftBatteryLevel":76,"leftChargingStatusDesc":"未充电"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "查看耳机电量，显示耳机名称、耳机盒电量、左右耳电量及充电状态。",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "earphone": {
        "earphoneName": {
          "type": "string",
          "description": "耳机的设备广播名称，如果未连接则返回'未连接耳机'。如: 'FreeBuds Pro 3'。",
          "sampleValue": "示例耳机"
        },
        "batteryLevel": {
          "type": "integer",
          "description": "耳机盒（或整体）当前剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”。若直接用于文本展示，必须在数值后追加“%”。",
          "sampleValue": 80
        },
        "chargingStatusDesc": {
          "type": "string",
          "description": "耳机盒（或整体）当前的充电状态中文语义描述，'充电中' 或 '未充电'。",
          "sampleValue": "未充电"
        },
        "leftBatteryLevel": {
          "type": "integer",
          "description": "左耳机当前剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”；未连接时为 0。若直接用于文本展示，必须在数值后追加“%”。",
          "sampleValue": 76
        },
        "leftChargingStatusDesc": {
          "type": "string",
          "description": "左耳机当前的充电状态中文语义描述，'充电中' 或 '未充电'。",
          "sampleValue": "未充电"
        },
        "rightBatteryLevel": {
          "type": "integer",
          "description": "右耳机当前剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”；未连接时为 0。若直接用于文本展示，必须在数值后追加“%”。",
          "sampleValue": 78
        },
        "rightChargingStatusDesc": {
          "type": "string",
          "description": "右耳机当前的充电状态中文语义描述，'充电中' 或 '未充电'。",
          "sampleValue": "未充电"
        }
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.emoji_bluetooth_earbuds_black",
      "src": "resources/base/media/emoji_bluetooth_earbuds_black.png",
      "description": "样式：深灰到黑色渐变的一对分体式入耳蓝牙耳机，带立体高光与透明背景，原始尺寸为 64×64，PNG 位图需保留原色；适用：蓝牙耳机连接状态、名称或左右耳电量卡片，可结合 GetEarphoneInfo 的 isConnected、earphoneName、leftBatteryLevel 和 rightBatteryLevel 展示，也可作为 event.open.settings.bluetooth 的蓝牙设置入口。图标不表示耳机当前已连接、正在充电或具有特定电量。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "GetEarphoneInfo"
  ],
  "event": [],
  "asset": [
    "asset.emoji_bluetooth_earbuds_black"
  ]
}
```
```removedcapabilities
[]
```
```generationplan
{
  "candidateDataBindings": [
    {
      "capabilityId": "GetEarphoneInfo",
      "arguments": {},
      "writeResultTo": "/data/earphone",
      "candidateOutputFields": [
        "/earphoneName",
        "/batteryLevel",
        "/chargingStatusDesc",
        "/leftBatteryLevel",
        "/leftChargingStatusDesc",
        "/rightBatteryLevel",
        "/rightChargingStatusDesc"
      ]
    }
  ],
  "candidateEventCandidates": [],
  "candidateAssetIds": [
    "asset.emoji_bluetooth_earbuds_black"
  ]
}
```
```meta
{
  "apiVersion": "v1",
  "taskSpecVersion": "task-spec-v1",
  "cardSpecVersion": "card-spec-v1",
  "dslProtocolVersion": "v0.9",
  "skillVersion": "skill-widget-v1",
  "protocolProfileId": "a2ui-form-rom6.0-v1",
  "capabilityRegistryVersion": "app-11.7.7.300_rom-7.0",
  "artifactSchemaVersion": "widget-artifact-v2",
  "generationMode": "create",
  "artifactId": "3badd1af-1c1e-49c3-9438-7e6ee948520d",
  "createdAt": 1793952373761
}
```
```designcompactdsl
["root","Layout",{"layout":"S-dual-info"},["first","second"]]
["first","InfoBlock",{"surfaceRole":"panel","primaryText":"{{ ${/data/earphone/batteryLevel} + '%' }}","secondaryText":"{{ '耳机盒 ' + ${/data/earphone/chargingStatusDesc} }}"}]
["second","InfoBlock",{"surfaceRole":"panel","primaryText":"{{ '左耳 ' + ${/data/earphone/leftBatteryLevel} + '%' }}","secondaryText":"{{ '左耳 ' + ${/data/earphone/leftChargingStatusDesc} }}"}]
["/data/earphone/batteryLevel",80]
["/data/earphone/chargingStatusDesc","未充电"]
["/data/earphone/leftBatteryLevel",76]
["/data/earphone/leftChargingStatusDesc","未充电"]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMM-AL10P 7.0.0.111",
    "candidateAssetIds": [
      "asset.emoji_bluetooth_earbuds_black"
    ],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "耳机状态速览",
    "userQuery": "查看耳机电量，显示耳机名称、耳机盒电量、左右耳电量及充电状态。",
    "title": "耳机电量",
    "candidateDataBindings": [
      {
        "capabilityId": "GetEarphoneInfo",
        "arguments": {},
        "writeResultTo": "/data/earphone",
        "candidateOutputFields": [
          "/earphoneName",
          "/batteryLevel",
          "/chargingStatusDesc",
          "/leftBatteryLevel",
          "/leftChargingStatusDesc",
          "/rightBatteryLevel",
          "/rightChargingStatusDesc"
        ]
      }
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMM-AL10",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261101080248254"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q514-000",
    "isNew": true,
    "sessionId": "batch-13ea8cbd"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "",
    "type": "text"
  },
  "version": "1.0",
  "size": "2x2",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMM-AL10P 7.0.0.111",
  "candidateAssetIds": [
    "asset.emoji_bluetooth_earbuds_black"
  ],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "耳机状态速览",
  "userQuery": "查看耳机电量，显示耳机名称、耳机盒电量、左右耳电量及充电状态。",
  "title": "耳机电量",
  "candidateDataBindings": [
    {
      "capabilityId": "GetEarphoneInfo",
      "arguments": {},
      "writeResultTo": "/data/earphone",
      "candidateOutputFields": [
        "/earphoneName",
        "/batteryLevel",
        "/chargingStatusDesc",
        "/leftBatteryLevel",
        "/leftChargingStatusDesc",
        "/rightBatteryLevel",
        "/rightChargingStatusDesc"
      ]
    }
  ]
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"S-title-dual-content\"},[\"title\",\"primary\",\"support\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":{\"path\":\"/data/earphone/earphoneName\"},\"icon\":\"resources/base/media/emoji_bluetooth_earbuds_black.png\",\"fontSize\":12}]\n[\"primary\",\"InfoBlock\",{\"surfaceRole\":\"panel\",\"primaryText\":\"{{ ${/data/earphone/batteryLevel} + '%' }}\",\"secondaryText\":\"{{ '耳机盒 ' + ${/data/earphone/chargingStatusDesc} }}\"}]\n[\"support\",\"SecondaryBody\",{\"items\":[{\"label\":\"左耳 \",\"value\":\"{{ ${/data/earphone/leftBatteryLevel} + '% ' + ${/data/earphone/leftChargingStatusDesc} }}\"},{\"label\":\"右耳 \",\"value\":\"{{ ${/data/earphone/rightBatteryLevel} + '% ' + ${/data/earphone/rightChargingStatusDesc} }}\"}],\"columns\":1,\"fontSize\":12}]\n[\"/data/earphone/earphoneName\",\"示例耳机\"]\n[\"/data/earphone/batteryLevel\",80]\n[\"/data/earphone/chargingStatusDesc\",\"未充电\"]\n[\"/data/earphone/leftBatteryLevel\",76]\n[\"/data/earphone/leftChargingStatusDesc\",\"未充电\"]\n[\"/data/earphone/rightBatteryLevel\",78]\n[\"/data/earphone/rightChargingStatusDesc\",\"未充电\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "语义布局不符合合同：节点 root：两个 InfoBlock 必须使用 stacked-info 变体。请选择已登记的 Layout、Region 或 Group 变体，不要修改展开后的几何。"
    }
  ]
}
```
```repair-2
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"S-title-dual-content\"},[\"title\",\"content\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":{\"path\":\"/data/earphone/earphoneName\"},\"icon\":\"resources/base/media/emoji_bluetooth_earbuds_black.png\",\"fontSize\":12}]\n[\"content\",\"Group\",{\"variant\":\"supporting-items\"},[\"content_item_1\",\"content_item_2\",\"content_item_3\"]]\n[\"content_item_1\",\"InfoBlock\",{\"surfaceRole\":\"panel\",\"primaryText\":\"{{ ${/data/earphone/batteryLevel} + '%' }}\",\"secondaryText\":\"{{ '耳机盒 ' + ${/data/earphone/chargingStatusDesc} }}\"}]\n[\"content_item_2\",\"InfoBlock\",{\"surfaceRole\":\"panel\",\"primaryText\":\"{{ ${/data/earphone/leftBatteryLevel} + '%' }}\",\"secondaryText\":\"{{ '左耳 ' + ${/data/earphone/leftChargingStatusDesc} }}\"}]\n[\"content_item_3\",\"InfoBlock\",{\"surfaceRole\":\"panel\",\"primaryText\":\"{{ ${/data/earphone/rightBatteryLevel} + '%' }}\",\"secondaryText\":\"{{ '右耳 ' + ${/data/earphone/rightChargingStatusDesc} }}\"}]\n[\"/data/earphone/earphoneName\",\"示例耳机\"]\n[\"/data/earphone/batteryLevel\",80]\n[\"/data/earphone/chargingStatusDesc\",\"未充电\"]\n[\"/data/earphone/leftBatteryLevel\",76]\n[\"/data/earphone/leftChargingStatusDesc\",\"未充电\"]\n[\"/data/earphone/rightBatteryLevel\",78]\n[\"/data/earphone/rightChargingStatusDesc\",\"未充电\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "语义布局不符合合同：节点 root：子组件数量应为 [3]；要求的 children 角色为 [title, primary, support]。请选择已登记的 Layout、Region 或 Group 变体，不要修改展开后的几何。"
    }
  ]
}
```
```repair-3
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"S-title-dual-content\"},[\"title\",\"primary\",\"support\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":{\"path\":\"/data/earphone/earphoneName\"},\"icon\":\"resources/base/media/emoji_bluetooth_earbuds_black.png\",\"fontSize\":12}]\n[\"primary\",\"InfoBlock\",{\"surfaceRole\":\"panel\",\"primaryText\":\"{{ ${/data/earphone/batteryLevel} + '%' }}\",\"secondaryText\":\"{{ '耳机盒 ' + ${/data/earphone/chargingStatusDesc} }}\"}]\n[\"support\",\"SecondaryBody\",{\"items\":[{\"label\":\"左耳 \",\"value\":\"{{ ${/data/earphone/leftBatteryLevel} + '% ' + ${/data/earphone/leftChargingStatusDesc} }}\"},{\"label\":\"右耳 \",\"value\":\"{{ ${/data/earphone/rightBatteryLevel} + '% ' + ${/data/earphone/rightChargingStatusDesc} }}\"}],\"columns\":1,\"fontSize\":12}]\n[\"/data/earphone/earphoneName\",\"示例耳机\"]\n[\"/data/earphone/batteryLevel\",80]\n[\"/data/earphone/chargingStatusDesc\",\"未充电\"]\n[\"/data/earphone/leftBatteryLevel\",76]\n[\"/data/earphone/leftChargingStatusDesc\",\"未充电\"]\n[\"/data/earphone/rightBatteryLevel\",78]\n[\"/data/earphone/rightChargingStatusDesc\",\"未充电\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "语义布局不符合合同：节点 root：两个 InfoBlock 必须使用 stacked-info 变体。请选择已登记的 Layout、Region 或 Group 变体，不要修改展开后的几何。"
    }
  ]
}
```
```repair-4
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"S-dual-info\"},[\"first\",\"second\"]]\n[\"first\",\"InfoBlock\",{\"surfaceRole\":\"panel\",\"primaryText\":\"{{ ${/data/earphone/batteryLevel} + '%' }}\",\"secondaryText\":\"{{ '耳机盒 ' + ${/data/earphone/chargingStatusDesc} }}\"}]\n[\"second\",\"InfoBlock\",{\"surfaceRole\":\"panel\",\"primaryText\":\"{{ '左耳 ' + ${/data/earphone/leftBatteryLevel} + '%' }}\",\"secondaryText\":\"{{ '左耳 ' + ${/data/earphone/leftChargingStatusDesc} }}\"}]\n[\"/data/earphone/batteryLevel\",80]\n[\"/data/earphone/chargingStatusDesc\",\"未充电\"]\n[\"/data/earphone/leftBatteryLevel\",76]\n[\"/data/earphone/leftChargingStatusDesc\",\"未充电\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"first\",\"second\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"borderRadius\":20,\"clip\":true,\"alignItems\":\"start\",\"justifyContent\":\"start\",\"padding\":8}},{\"id\":\"first\",\"component\":\"Column\",\"children\":[\"first_text\"],\"itemMargin\":0,\"styles\":{\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"clip\":true,\"flexShrink\":0,\"width\":\"matchParent\",\"height\":63,\"backgroundColor\":\"@theme:panel/1\",\"layoutWeight\":1}},{\"id\":\"first_text\",\"component\":\"Column\",\"children\":[\"first_primary\",\"first_secondary\"],\"itemMargin\":0,\"styles\":{\"alignItems\":\"start\",\"justifyContent\":\"center\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"first_primary\",\"component\":\"Text\",\"content\":\"{{ ${/data/earphone/batteryLevel} + '%' }}\",\"styles\":{\"height\":22,\"fontSize\":16,\"fontWeight\":700,\"maxLines\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"first_secondary\",\"component\":\"Text\",\"content\":\"{{ '耳机盒 ' + ${/data/earphone/chargingStatusDesc} }}\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":500,\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"second\",\"component\":\"Column\",\"children\":[\"second_text\"],\"itemMargin\":0,\"styles\":{\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"clip\":true,\"flexShrink\":0,\"width\":\"matchParent\",\"height\":63,\"backgroundColor\":\"@theme:panel/1\",\"layoutWeight\":1}},{\"id\":\"second_text\",\"component\":\"Column\",\"children\":[\"second_primary\",\"second_secondary\"],\"itemMargin\":0,\"styles\":{\"alignItems\":\"start\",\"justifyContent\":\"center\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"second_primary\",\"component\":\"Text\",\"content\":\"{{ '左耳 ' + ${/data/earphone/leftBatteryLevel} + '%' }}\",\"styles\":{\"height\":22,\"fontSize\":16,\"fontWeight\":700,\"maxLines\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"second_secondary\",\"component\":\"Text\",\"content\":\"{{ '左耳 ' + ${/data/earphone/leftChargingStatusDesc} }}\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":500,\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"earphone\":{\"batteryLevel\":80,\"chargingStatusDesc\":\"未充电\",\"leftBatteryLevel\":76,\"leftChargingStatusDesc\":\"未充电\"}}}}}",
  "validationErrors": []
}
```
