```cardspec
{
  "title": "透明时间",
  "description": "透明时间卡片",
  "suggestSize": "2x4",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"当前时间","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__details"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary","component":"Column","children":["primary_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"primary_main","component":"Text","content":"{{ ${/data/time/currentDate} }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__details","component":"Column","children":["details"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"details","component":"Row","children":["details_item0","details_item1"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","alignItems":"top","justifyContent":"start","layoutWeight":1,"flexShrink":1,"constraintSize":{"minHeight":48}}},{"id":"details_item0","component":"Column","children":["details_item0_label_slot","details_item0_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item0_label_slot","component":"Row","children":["details_item0_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item0_label","component":"Text","content":"星期","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item0_value_slot","component":"Row","children":["details_item0_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item0_value","component":"Text","content":"{{ ${/data/time/dayOfWeek} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}},{"id":"details_item1","component":"Column","children":["details_item1_label_slot","details_item1_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item1_label_slot","component":"Row","children":["details_item1_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item1_label","component":"Text","content":"农历","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item1_value_slot","component":"Row","children":["details_item1_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item1_value","component":"Text","content":"{{ ${/data/time/lunarDate} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"currentDate":"示例","dayOfWeek":"示例","lunarDate":"示例"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "生成一个二乘四比例的透明的时间桌面卡片，显示当前时间和日期。",
  "size": "2x4",
  "appVersion": "11.7.8.342",
  "eventCandidates": [
    {
      "id": "event.open.clock.alarm",
      "description": "打开华为时钟应用首页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "com.huawei.hmos.clock.phone",
        "bundleName": "com.huawei.hmos.clock",
        "intentName": "Clock",
        "uri": ""
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
  "event": [
    {
      "id": "event.open.clock.alarm",
      "description": "打开华为时钟应用首页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "com.huawei.hmos.clock.phone",
        "bundleName": "com.huawei.hmos.clock",
        "intentName": "Clock",
        "uri": ""
      }
    }
  ],
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
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.clock.alarm",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "com.huawei.hmos.clock.phone",
          "bundleName": "com.huawei.hmos.clock",
          "intentName": "Clock",
          "uri": ""
        }
      }
    }
  ],
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
  "artifactId": "b70cc280-1755-454c-a541-905c48cfdfde",
  "createdAt": 1793934552315
}
```
```designcompactdsl
["root","Layout",{"layout":"W-top-bottom","variant":"continuous"},["title","primary","details"]]
["title","SingleLineTitle",{"title":"当前时间","fontSize":12}]
["primary","EmphasisText",{"mainText":{"path":"/data/time/currentDate"},"fontSize":18}]
["details","TextBlock",{"items":[{"label":"星期","value":{"path":"/data/time/dayOfWeek"}},{"label":"农历","value":{"path":"/data/time/lunarDate"}}]}]
["/data/time/currentDate","示例"]
["/data/time/dayOfWeek","示例"]
["/data/time/lunarDate","示例"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "生成一个二乘四比例的透明的时间桌面卡片，显示当前时间和日期。",
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
    "title": "透明时间",
    "size": "2x4",
    "candidateEventCandidates": [
      {
        "capabilityId": "event.open.clock.alarm",
        "action": {
          "call": "clickToDeeplink",
          "args": {
            "abilityName": "com.huawei.hmos.clock.phone",
            "bundleName": "com.huawei.hmos.clock",
            "intentName": "Clock",
            "uri": ""
          }
        }
      }
    ],
    "description": "透明时间卡片",
    "candidateAssetIds": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMM-AL10",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261029074846301"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q307-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "生成一个二乘四比例的透明的时间桌面卡片，显示当前时间和日期。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMM-AL10 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "生成一个二乘四比例的透明的时间桌面卡片，显示当前时间和日期。",
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
  "title": "透明时间",
  "size": "2x4",
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.clock.alarm",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "com.huawei.hmos.clock.phone",
          "bundleName": "com.huawei.hmos.clock",
          "intentName": "Clock",
          "uri": ""
        }
      }
    }
  ],
  "description": "透明时间卡片",
  "candidateAssetIds": []
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"title\",\"primary\",\"details\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":\"当前时间\",\"fontSize\":12}]\n[\"primary\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/time/currentDate\"},\"secondaryText\":{\"path\":\"/data/time/dayOfWeek\"},\"fontSize\":18}]\n[\"details\",\"SecondaryBody\",{\"items\":[{\"label\":\"农历 \",\"value\":{\"path\":\"/data/time/lunarDate\"}}],\"fontSize\":14}]\n[\"/data/time/currentDate\",\"示例\"]\n[\"/data/time/dayOfWeek\",\"示例\"]\n[\"/data/time/lunarDate\",\"示例\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "语义布局不符合合同：节点 details：details 槽必须使用 TextBlock、TopTextBottomValue、SummaryList 或 EventCard。请选择已登记的 Layout、Region 或 Group 变体，不要修改展开后的几何。"
    }
  ]
}
```
```repair-2
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"title\",\"primary\",\"details\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":\"当前时间\",\"fontSize\":12}]\n[\"primary\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/time/currentDate\"},\"secondaryText\":{\"path\":\"/data/time/dayOfWeek\"},\"fontSize\":18}]\n[\"details\",\"TextBlock\",{\"items\":[{\"label\":\"农历\",\"value\":{\"path\":\"/data/time/lunarDate\"}},{\"label\":\"星期\",\"value\":{\"path\":\"/data/time/dayOfWeek\"}}]}]\n[\"/data/time/currentDate\",\"示例\"]\n[\"/data/time/dayOfWeek\",\"示例\"]\n[\"/data/time/lunarDate\",\"示例\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_PLAN_COVERAGE_FAILED",
      "message": "Plan fact is displayed more than once in visible DSL: 显示当前星期 (/data/time/dayOfWeek); expected 1, got 2; occurrences: primary (EmphasisText).secondaryText, details (TextBlock).items[1].value.",
      "duplicateFacts": [
        {
          "requirement": "显示当前星期",
          "dataId": "/data/time/dayOfWeek",
          "expectedVisibleCount": 1,
          "actualVisibleCount": 2,
          "occurrences": [
            {
              "componentId": "primary",
              "componentType": "EmphasisText",
              "property": "secondaryText"
            },
            {
              "componentId": "details",
              "componentType": "TextBlock",
              "property": "items[1].value"
            }
          ],
          "ownershipInstruction": "按同一 dataId 选择唯一完整展示落点，保留已有对象标签、单位、绑定和动作；不得按相同样值去重，不得删除独有事实或造新事实填槽。若requiredDisplayPositions确认同一事实占据至少两个不同必填展示槽，不能清空属性、删除固定槽或放入占位文字；仅在repairStrategy允许范围内重新分配已有独立事实或调整必要父布局的合法组合，并补齐全部角色后完整复检。普通重复保持信息组内修复，不据此扩大为整卡重建。",
          "requiredDisplayPositions": []
        }
      ]
    }
  ]
}
```
```repair-3
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"title\",\"primary\",\"details\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":\"当前时间\",\"fontSize\":12}]\n[\"primary\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/time/currentDate\"},\"fontSize\":18}]\n[\"details\",\"TextBlock\",{\"items\":[{\"label\":\"星期\",\"value\":{\"path\":\"/data/time/dayOfWeek\"}},{\"label\":\"农历\",\"value\":{\"path\":\"/data/time/lunarDate\"}}]}]\n[\"/data/time/currentDate\",\"示例\"]\n[\"/data/time/dayOfWeek\",\"示例\"]\n[\"/data/time/lunarDate\",\"示例\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"title\",\"__layout__root__body\"],\"itemMargin\":6,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"start\",\"justifyContent\":\"start\"}},{\"id\":\"title\",\"component\":\"Row\",\"children\":[\"title_title\"],\"styles\":{\"width\":\"matchParent\",\"height\":12,\"flexShrink\":0,\"justifyContent\":\"start\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"title_title\",\"component\":\"Text\",\"content\":\"当前时间\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":0,\"width\":\"matchParent\",\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"__layout__root__body\",\"component\":\"Column\",\"children\":[\"__layout__root__primary\",\"__layout__root__details\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1}},{\"id\":\"__layout__root__primary\",\"component\":\"Column\",\"children\":[\"primary\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"primary\",\"component\":\"Column\",\"children\":[\"primary_main\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"primary_main\",\"component\":\"Text\",\"content\":\"{{ ${/data/time/currentDate} }}\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"__layout__root__details\",\"component\":\"Column\",\"children\":[\"details\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"details\",\"component\":\"Row\",\"children\":[\"details_item0\",\"details_item1\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"alignItems\":\"top\",\"justifyContent\":\"start\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minHeight\":48}}},{\"id\":\"details_item0\",\"component\":\"Column\",\"children\":[\"details_item0_label_slot\",\"details_item0_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item0_label_slot\",\"component\":\"Row\",\"children\":[\"details_item0_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item0_label\",\"component\":\"Text\",\"content\":\"星期\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item0_value_slot\",\"component\":\"Row\",\"children\":[\"details_item0_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item0_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/time/dayOfWeek} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"details_item1\",\"component\":\"Column\",\"children\":[\"details_item1_label_slot\",\"details_item1_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item1_label_slot\",\"component\":\"Row\",\"children\":[\"details_item1_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item1_label\",\"component\":\"Text\",\"content\":\"农历\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item1_value_slot\",\"component\":\"Row\",\"children\":[\"details_item1_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item1_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/time/lunarDate} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"time\":{\"currentDate\":\"示例\",\"dayOfWeek\":\"示例\",\"lunarDate\":\"示例\"}}}}}",
  "validationErrors": []
}
```
