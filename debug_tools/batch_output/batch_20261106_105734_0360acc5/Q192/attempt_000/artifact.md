```cardspec
{
  "title": "新年倒计时",
  "description": "距离新年还有",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-01-01"
      },
      "writeResultTo": "/data/countdown"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFFFE0CC",0],["#FFFFF7F2",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"新年倒计时","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#998C4B1C"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__support"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1,"flexShrink":0},"itemMargin":0},{"id":"primary","component":"Row","children":["primary_value","primary_unit"],"itemMargin":2,"styles":{"justifyContent":"start","alignItems":"bottom","flexShrink":0,"width":"matchParent"}},{"id":"primary_value","component":"Text","content":"{{ ${/data/countdown/countdownDays} }}","styles":{"height":30,"fontSize":30,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#FF8C4B1C","textOverflow":"clip"}},{"id":"primary_unit","component":"Text","content":"天","styles":{"height":13.75,"fontSize":12,"fontWeight":500,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#998C4B1C","padding":{"top":0,"right":0,"bottom":1.75,"left":0},"textOverflow":"clip"}},{"id":"__layout__root__support","component":"Column","children":["support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"support","component":"Column","children":["support_row0"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"support_item0_value","component":"Text","content":"距离2027年1月1日新年倒计时","styles":{"height":24.0,"fontSize":12,"fontWeight":400,"maxLines":2,"flexShrink":1,"lineHeight":1,"fontColor":"#998C4B1C","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item0","component":"Row","children":["support_item0_value"],"itemMargin":0,"styles":{"height":24.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row0","component":"Row","children":["support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":24.0,"alignItems":"top","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"countdown":{"countdownDays":30}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "帮我生成一张新年卡片，展示距离2027年1月1日新年的倒计时天数。\n\n本轮卡片静态内容（用作展示的外部事实）：\n距离2027年1月1日新年倒计时",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "countdown": {
        "countdownDays": {
          "type": "integer",
          "description": "距离目标日期的自然日天数纯整数，返回值不包含“天”。正数表示未来，0 表示今天，负数表示已经过去；若直接用于文本展示，必须在数值后追加“天”。",
          "sampleValue": 30
        }
      }
    }
  },
  "assetCandidates": []
}
```
```effectivecapabilities
{
  "data": [
    "GetCountdownDays"
  ],
  "event": [],
  "asset": []
}
```
```removedcapabilities
[]
```
```generationplan
{
  "candidateDataBindings": [
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-01-01"
      },
      "writeResultTo": "/data/countdown",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    }
  ],
  "candidateEventCandidates": [],
  "candidateAssetIds": []
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
  "artifactId": "bc6a6a22-4d1a-40f2-bc22-09da3605f807",
  "createdAt": 1793933868430
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-dual-content"},["title","primary","support"]]
["title","SingleLineTitle",{"title":"新年倒计时","fontSize":12}]
["primary","EmphasizedData",{"value":{"path":"/data/countdown/countdownDays"},"unit":"天","fontSize":30}]
["support","SecondaryBody",{"items":[{"value":"距离2027年1月1日新年倒计时","maxLines":2}],"fontSize":12}]
["/data/countdown/countdownDays",30]
```
```request
{
  "content": {
    "title": "新年倒计时",
    "description": "距离新年还有",
    "userQuery": "帮我生成一张新年卡片，展示距离2027年1月1日新年的倒计时天数。\n\n本轮卡片静态内容（用作展示的外部事实）：\n距离2027年1月1日新年倒计时",
    "size": "2x2",
    "bundleName": "com.huawei.genui",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMM-AL00 7.0.0.111",
    "candidateDataBindings": [
      {
        "arguments": {
          "targetDate": "2027-01-01"
        },
        "candidateOutputFields": [
          "/countdownDays"
        ],
        "capabilityId": "GetCountdownDays",
        "writeResultTo": "/data/countdown"
      }
    ],
    "candidateEventCandidates": [],
    "candidateAssetIds": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMM-AL00",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261025000445868"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q192-000",
    "isNew": true,
    "sessionId": "batch-0360acc5"
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
  "romVersion": "CMM-AL00 7.0.0.111",
  "candidateAssetIds": [],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "距离新年还有",
  "userQuery": "帮我生成一张新年卡片，展示距离2027年1月1日新年的倒计时天数。\n\n本轮卡片静态内容（用作展示的外部事实）：\n距离2027年1月1日新年倒计时",
  "title": "新年倒计时",
  "candidateDataBindings": [
    {
      "arguments": {
        "targetDate": "2027-01-01"
      },
      "candidateOutputFields": [
        "/countdownDays"
      ],
      "capabilityId": "GetCountdownDays",
      "writeResultTo": "/data/countdown"
    }
  ]
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"S-title-dual-content\"},[\"title\",\"primary\",\"support\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":\"新年倒计时\",\"fontSize\":12}]\n[\"primary\",\"EmphasizedData\",{\"value\":{\"path\":\"/data/countdown/countdownDays\"},\"unit\":\"天\",\"fontSize\":30}]\n[\"support\",\"SecondaryBody\",{\"items\":[{\"value\":\"距离2027年1月1日新年倒计时\",\"maxLines\":2}],\"fontSize\":12}]\n[\"/data/countdown/countdownDays\",30]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"title\",\"__layout__root__body\"],\"itemMargin\":6,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"borderRadius\":20,\"clip\":true,\"alignItems\":\"start\",\"justifyContent\":\"start\",\"padding\":12}},{\"id\":\"title\",\"component\":\"Row\",\"children\":[\"title_title\"],\"styles\":{\"width\":\"matchParent\",\"height\":12,\"flexShrink\":0,\"justifyContent\":\"start\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"title_title\",\"component\":\"Text\",\"content\":\"新年倒计时\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":0,\"width\":\"matchParent\",\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"__layout__root__body\",\"component\":\"Column\",\"children\":[\"__layout__root__primary\",\"__layout__root__support\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1}},{\"id\":\"__layout__root__primary\",\"component\":\"Column\",\"children\":[\"primary\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1,\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"primary\",\"component\":\"Row\",\"children\":[\"primary_value\",\"primary_unit\"],\"itemMargin\":2,\"styles\":{\"justifyContent\":\"start\",\"alignItems\":\"bottom\",\"flexShrink\":0,\"width\":\"matchParent\"}},{\"id\":\"primary_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/countdown/countdownDays} }}\",\"styles\":{\"height\":30,\"fontSize\":30,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":0,\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"primary_unit\",\"component\":\"Text\",\"content\":\"天\",\"styles\":{\"height\":13.75,\"fontSize\":12,\"fontWeight\":500,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":0,\"fontColor\":\"@theme:primary/0.6\",\"padding\":{\"top\":0,\"right\":0,\"bottom\":1.75,\"left\":0},\"textOverflow\":\"clip\"}},{\"id\":\"__layout__root__support\",\"component\":\"Column\",\"children\":[\"support\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"support\",\"component\":\"Column\",\"children\":[\"support_row0\"],\"itemMargin\":2,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"flexShrink\":1}},{\"id\":\"support_item0_value\",\"component\":\"Text\",\"content\":\"距离2027年1月1日新年倒计时\",\"styles\":{\"height\":24.0,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":2,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/0.6\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"support_item0\",\"component\":\"Row\",\"children\":[\"support_item0_value\"],\"itemMargin\":0,\"styles\":{\"height\":24.0,\"alignItems\":\"top\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"support_row0\",\"component\":\"Row\",\"children\":[\"support_item0\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":24.0,\"alignItems\":\"top\",\"flexShrink\":0}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"countdown\":{\"countdownDays\":30}}}}}",
  "validationErrors": []
}
```
