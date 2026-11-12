```cardspec
{
  "title": "倒计时",
  "description": "三个月倒计时",
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
        "targetDate": "2027-02-03"
      },
      "writeResultTo": "/data/countdown"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Stack","children":["fusionBallBackground","__genui_render_component__root"],"styles":{"width":"matchParent","height":"matchParent","padding":0,"alignContent":"topStart","clip":true,"borderRadius":20,"backgroundColor":"#00000000"}},{"id":"fusionBallBackground","component":"Stack","children":["fusionBallLargeSlot","fusionBallMediumSlot","fusionBallSmallSlot","fusionBallGlassLayer"],"styles":{"width":"100%","height":"100%","borderRadius":20,"alignContent":"topStart","clip":true}},{"id":"fusionBallLargeSlot","component":"Stack","children":["fusionBallLarge"],"styles":{"width":"112.5%","height":"27.5%","alignContent":"center"}},{"id":"fusionBallLarge","component":"Divider","styles":{"width":"116.666667%","height":"477.272727%","strokeWidth":0,"color":"#00000000","borderRadius":105,"backgroundColor":"#FFF24131","clip":true}},{"id":"fusionBallMediumSlot","component":"Stack","children":["fusionBallMedium"],"styles":{"width":"50%","height":"137.5%","alignContent":"bottom"}},{"id":"fusionBallMedium","component":"Divider","styles":{"width":"200%","height":"72.727273%","strokeWidth":0,"color":"#00000000","borderRadius":80,"backgroundColor":"#FFFF8833","clip":true}},{"id":"fusionBallSmallSlot","component":"Stack","children":["fusionBallSmall"],"styles":{"width":"121.875%","height":"118.75%","alignContent":"bottomEnd"}},{"id":"fusionBallSmall","component":"Divider","styles":{"width":"51.282051%","height":"52.631579%","strokeWidth":0,"color":"#00000000","borderRadius":50,"backgroundColor":"#FFE68073","clip":true}},{"id":"fusionBallGlassLayer","component":"Divider","styles":{"width":"100%","height":"100%","strokeWidth":0,"color":"#00000000","backgroundColor":"#0DFFFFFF","backdropBlur":{"radius":210}}},{"id":"__genui_render_component__root","component":"Column","children":["content"],"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"center","padding":12},"itemMargin":0},{"id":"content","component":"Column","children":["content_label","content_value","content_supporting"],"itemMargin":8,"styles":{"width":"matchParent","height":114,"alignItems":"center","justifyContent":"center","flexShrink":1}},{"id":"content_label","component":"Text","content":"倒计时","styles":{"width":"matchParent","height":18,"fontSize":12,"fontWeight":500,"textAlign":"center","maxLines":1,"fontColor":"#99FFFFFF","textOverflow":"clip"}},{"id":"content_value","component":"Text","content":"{{ ${/data/countdown/countdownDays} }}","styles":{"height":60,"fontSize":48,"fontWeight":700,"textAlign":"center","maxLines":1,"width":"matchParent","fontColor":"#FFFFFFFF","textOverflow":"clip"}},{"id":"content_supporting","component":"Text","content":"天","styles":{"height":20,"fontSize":14,"fontWeight":400,"textAlign":"center","maxLines":1,"width":"matchParent","fontColor":"#99FFFFFF","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"countdown":{"countdownDays":30}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "制作一张倒计时卡片，从明天开始倒计时三个月，目标日期为2027年2月3日，显示距离目标日期还有多少天。",
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
        "targetDate": "2027-02-03"
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
  "artifactId": "d0bcb797-047c-48d8-b0d5-67690fe363f0",
  "createdAt": 1793952241031
}
```
```designcompactdsl
["root","Layout",{"layout":"S-center"},["content"]]
["content","DataDisplay",{"label":"倒计时","value":{"path":"/data/countdown/countdownDays"},"supportingText":"天"}]
["/data/countdown/countdownDays",30]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMM-AL00 7.0.0.111",
    "candidateAssetIds": [],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "三个月倒计时",
    "userQuery": "制作一张倒计时卡片，从明天开始倒计时三个月，目标日期为2027年2月3日，显示距离目标日期还有多少天。",
    "title": "倒计时",
    "candidateDataBindings": [
      {
        "capabilityId": "GetCountdownDays",
        "arguments": {
          "targetDate": "2027-02-03"
        },
        "writeResultTo": "/data/countdown",
        "candidateOutputFields": [
          "/countdownDays"
        ]
      }
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMM-AL00",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261102091156385"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q472-000",
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
  "romVersion": "CMM-AL00 7.0.0.111",
  "candidateAssetIds": [],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "三个月倒计时",
  "userQuery": "制作一张倒计时卡片，从明天开始倒计时三个月，目标日期为2027年2月3日，显示距离目标日期还有多少天。",
  "title": "倒计时",
  "candidateDataBindings": [
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-02-03"
      },
      "writeResultTo": "/data/countdown",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    }
  ]
}
```
