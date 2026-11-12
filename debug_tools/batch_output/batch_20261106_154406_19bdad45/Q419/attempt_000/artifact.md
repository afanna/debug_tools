```cardspec
{
  "title": "当前时间",
  "description": "实时时间显示",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["content"],"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"center","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}},"itemMargin":0},{"id":"content","component":"Column","children":["content_label","content_value_area","content_supporting"],"itemMargin":8,"styles":{"width":"matchParent","height":122,"alignItems":"center","justifyContent":"center","flexShrink":1}},{"id":"content_label","component":"Text","content":"当前日期","styles":{"width":"matchParent","height":18,"fontSize":12,"fontWeight":500,"textAlign":"center","maxLines":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"content_value_area","component":"Column","children":["content_value"],"styles":{"width":"matchParent","height":60,"alignItems":"center","justifyContent":"center","flexShrink":0},"itemMargin":0},{"id":"content_value","component":"Text","content":"{{ ${/data/time/currentDate} }}","styles":{"fontSize":21,"fontWeight":700,"textAlign":"center","maxLines":2,"width":"matchParent","lineHeight":1.25,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"content_supporting","component":"Text","content":"{{ ${/data/time/dayOfWeek} }}","styles":{"height":20,"fontSize":14,"fontWeight":400,"textAlign":"center","maxLines":1,"width":"matchParent","margin":{"top":8,"right":0,"bottom":0,"left":0},"flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"currentDate":"示例","dayOfWeek":"示例"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "做一张时间卡片，显示当前日期、时间和星期。",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "time": {
        "currentDate": {
          "type": "string",
          "description": "格式化的当前公历日期（年-月-日），例如 '2026-07-09'。",
          "sampleValue": "示例"
        },
        "dayOfWeek": {
          "type": "string",
          "description": "中文的星期描述，例如 '星期四'。",
          "sampleValue": "示例"
        },
        "lunarDate": {
          "type": "string",
          "description": "格式化的中国传统农历日期，例如 '五月廿六'。若系统获取失败则可能为空字符串。",
          "sampleValue": "示例"
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
    "GetCurrentTime"
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
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time",
      "candidateOutputFields": [
        "/currentDate",
        "/dayOfWeek",
        "/lunarDate"
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
  "artifactId": "d842f19d-c10e-4833-a906-7216cd85a9de",
  "createdAt": 1793951206228
}
```
```designcompactdsl
["root","Layout",{"layout":"S-center"},["content"]]
["content","DataDisplay",{"label":"当前日期","value":{"path":"/data/time/currentDate"},"supportingText":{"path":"/data/time/dayOfWeek"}}]
["/data/time/currentDate","示例"]
["/data/time/dayOfWeek","示例"]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMS-AL20 7.0.0.111",
    "candidateAssetIds": [],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "实时时间显示",
    "userQuery": "做一张时间卡片，显示当前日期、时间和星期。",
    "title": "当前时间",
    "candidateDataBindings": [
      {
        "capabilityId": "GetCurrentTime",
        "arguments": {},
        "writeResultTo": "/data/time",
        "candidateOutputFields": [
          "/currentDate",
          "/dayOfWeek",
          "/lunarDate"
        ]
      }
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMS-AL20",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261031170012557"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q419-000",
    "isNew": true,
    "sessionId": "batch-19bdad45"
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
  "romVersion": "CMS-AL20 7.0.0.111",
  "candidateAssetIds": [],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "实时时间显示",
  "userQuery": "做一张时间卡片，显示当前日期、时间和星期。",
  "title": "当前时间",
  "candidateDataBindings": [
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time",
      "candidateOutputFields": [
        "/currentDate",
        "/dayOfWeek",
        "/lunarDate"
      ]
    }
  ]
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"S-center\"},[\"content\"]]\n[\"content\",\"DataDisplay\",{\"label\":\"当前日期\",\"value\":{\"path\":\"/data/time/currentDate\"},\"supportingText\":{\"path\":\"/data/time/dayOfWeek\"}}]\n[\"/data/time/currentDate\",\"示例\"]\n[\"/data/time/dayOfWeek\",\"示例\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"content\"],\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"borderRadius\":20,\"clip\":true,\"alignItems\":\"center\",\"justifyContent\":\"center\",\"padding\":12},\"itemMargin\":0},{\"id\":\"content\",\"component\":\"Column\",\"children\":[\"content_label\",\"content_value_area\",\"content_supporting\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"height\":122,\"alignItems\":\"center\",\"justifyContent\":\"center\",\"flexShrink\":1}},{\"id\":\"content_label\",\"component\":\"Text\",\"content\":\"当前日期\",\"styles\":{\"width\":\"matchParent\",\"height\":18,\"fontSize\":12,\"fontWeight\":500,\"textAlign\":\"center\",\"maxLines\":1,\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"clip\"}},{\"id\":\"content_value_area\",\"component\":\"Column\",\"children\":[\"content_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":60,\"alignItems\":\"center\",\"justifyContent\":\"center\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"content_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/time/currentDate} }}\",\"styles\":{\"fontSize\":21,\"fontWeight\":700,\"textAlign\":\"center\",\"maxLines\":2,\"width\":\"matchParent\",\"lineHeight\":1.25,\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"content_supporting\",\"component\":\"Text\",\"content\":\"{{ ${/data/time/dayOfWeek} }}\",\"styles\":{\"height\":20,\"fontSize\":14,\"fontWeight\":400,\"textAlign\":\"center\",\"maxLines\":1,\"width\":\"matchParent\",\"margin\":{\"top\":8,\"right\":0,\"bottom\":0,\"left\":0},\"flexShrink\":0,\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"time\":{\"currentDate\":\"示例\",\"dayOfWeek\":\"示例\"}}}}}",
  "validationErrors": []
}
```
