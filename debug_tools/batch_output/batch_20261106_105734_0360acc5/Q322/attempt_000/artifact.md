```cardspec
{
  "title": "小艺",
  "description": "小艺快捷入口",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"手电筒","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__action"],"itemMargin":0,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"end","layoutWeight":1}},{"id":"__layout__root__action","component":"Column","children":["action"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","height":36,"flexShrink":0},"itemMargin":0},{"id":"action","component":"Row","children":["action_icon","action_text"],"onClick":[{"call":"clickToIntent","args":{"intentName":"OpenFlashlight","params":{}}}],"itemMargin":8,"styles":{"height":36,"borderRadius":30,"padding":0,"flexShrink":0,"width":"matchParent","backgroundColor":"#331F4799","justifyContent":"center","alignItems":"center"}},{"id":"action_icon","component":"Image","src":"resources/base/media/ic_flashlight.svg","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0,"fillColor":"#FF1F4799"}},{"id":"action_text","component":"Text","content":"打开手电筒","styles":{"maxWidth":96,"height":17,"fontSize":14,"fontWeight":500,"textAlign":"center","maxLines":1,"flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"state":{"ready":true}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "在手机桌面创建一个快捷入口卡片，点击可以打开手电筒",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [
    {
      "id": "event.openFlashlight",
      "description": "点击后打开手机手电筒",
      "call": "clickToIntent",
      "args": {
        "intentName": "OpenFlashlight",
        "params": {}
      }
    }
  ],
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
        },
        "updatedAt": {
          "type": "string",
          "description": "端侧完成该时间数据组装的时间戳字符串，格式如 '2026-07-09 15:30:00'。",
          "sampleValue": "示例"
        }
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.ic_flashlight",
      "src": "resources/base/media/ic_flashlight.svg",
      "description": "样式：默认黑色的单色手电筒图标，筒身为竖向圆角轮廓，原始尺寸为 24×24；适用：手电筒快捷控制卡片，可结合 event.openFlashlight 开启手电筒或 event.closeFlashlight 关闭手电筒。图标本身不表示手电筒当前开关状态。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "GetCurrentTime"
  ],
  "event": [
    {
      "id": "event.openFlashlight",
      "description": "点击后打开手机手电筒",
      "call": "clickToIntent",
      "args": {
        "intentName": "OpenFlashlight",
        "params": {}
      }
    }
  ],
  "asset": [
    "asset.ic_flashlight"
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
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time",
      "candidateOutputFields": []
    }
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.openFlashlight",
      "action": {
        "call": "clickToIntent",
        "args": {
          "intentName": "OpenFlashlight",
          "params": {}
        }
      }
    }
  ],
  "candidateAssetIds": [
    "asset.ic_flashlight"
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
  "artifactId": "8c76a379-5ea4-4f90-bbf2-ad1c0df0c910",
  "createdAt": 1793933878890
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-content-action","variant":"title-action"},["title","action"]]
["title","SingleLineTitle",{"title":"手电筒","fontSize":12}]
["action","PillButton",{"label":"打开手电筒","icon":"resources/base/media/ic_flashlight.svg","onClick":[{"call":"clickToIntent","args":{"intentName":"OpenFlashlight","params":{}}}]}]
["/state/ready",true]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "在手机桌面创建一个快捷入口卡片，点击可以打开手电筒",
    "candidateDataBindings": [
      {
        "capabilityId": "GetCurrentTime",
        "arguments": {},
        "writeResultTo": "/data/time"
      }
    ],
    "title": "小艺",
    "size": "2x2",
    "candidateEventCandidates": [
      {
        "capabilityId": "event.openFlashlight",
        "action": {
          "call": "clickToIntent",
          "args": {
            "intentName": "OpenFlashlight",
            "params": {}
          }
        }
      }
    ],
    "description": "小艺快捷入口",
    "candidateAssetIds": [
      "asset.ic_flashlight"
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "HLS-AL00",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261029143807181"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q322-000",
    "isNew": true,
    "sessionId": "batch-0360acc5"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "在手机桌面创建一个快捷入口卡片，点击可以打开手电筒",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "HLS-AL00 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "在手机桌面创建一个快捷入口卡片，点击可以打开手电筒",
  "candidateDataBindings": [
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time"
    }
  ],
  "title": "小艺",
  "size": "2x2",
  "candidateEventCandidates": [
    {
      "capabilityId": "event.openFlashlight",
      "action": {
        "call": "clickToIntent",
        "args": {
          "intentName": "OpenFlashlight",
          "params": {}
        }
      }
    }
  ],
  "description": "小艺快捷入口",
  "candidateAssetIds": [
    "asset.ic_flashlight"
  ]
}
```
