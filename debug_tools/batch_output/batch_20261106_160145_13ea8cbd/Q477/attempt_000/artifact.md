```cardspec
{
  "title": "天气预报",
  "description": "天气速览",
  "suggestSize": "2x4",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"{{ ${/data/weather/location/districtName} }}","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__details"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary","component":"Column","children":["primary_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"primary_main","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__details","component":"Column","children":["details"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"details","component":"Row","children":["details_item0","details_item1"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","alignItems":"top","justifyContent":"start","layoutWeight":1,"flexShrink":1,"constraintSize":{"minHeight":48}}},{"id":"details_item0","component":"Column","children":["details_item0_label_slot","details_item0_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item0_label_slot","component":"Row","children":["details_item0_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item0_label","component":"Text","content":"天气","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item0_value_slot","component":"Row","children":["details_item0_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item0_value","component":"Text","content":"{{ ${/data/weather/current/condition} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}},{"id":"details_item1","component":"Column","children":["details_item1_label_slot","details_item1_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item1_label_slot","component":"Row","children":["details_item1_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item1_label","component":"Text","content":"城市代码","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item1_value_slot","component":"Row","children":["details_item1_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item1_value","component":"Text","content":"{{ ${/data/weather/location/cityCode} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"weather":{"location":{"districtName":"青浦区","cityCode":"60814"},"current":{"temperatureText":"29℃","condition":"多云"}}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "把那个大框框设置天气预报，显示当前天气和温度。",
  "size": "2x4",
  "appVersion": "11.7.8.342",
  "eventCandidates": [
    {
      "id": "event.open.weather",
      "description": "打开华为天气应用某城市页，uri为固定值勿更改。cityCode来自于数据能力中ViewWeather出参cityCode字段，进行动态拼接，表示跳转到指定城市天气页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "",
        "bundleName": "",
        "intentName": "Weather_CityCode",
        "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
      }
    }
  ],
  "dataModelSchema": {
    "data": {
      "weather": {
        "current": {
          "temperatureText": {
            "type": "string",
            "description": "可直接显示的当前温度文本，已包含“℃”单位；展示时不得再次追加温度单位。例如“29℃”。",
            "sampleValue": "29℃"
          },
          "condition": {
            "type": "string",
            "description": "当前天气现象，例如“阴”“多云”“小雨”。",
            "sampleValue": "多云"
          }
        },
        "location": {
          "districtName": {
            "type": "string",
            "description": "区或县名称",
            "sampleValue": "青浦区"
          },
          "cityCode": {
            "type": "string",
            "description": "城市代码，如60814代表青浦区",
            "sampleValue": "60814"
          }
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
    "ViewWeather"
  ],
  "event": [
    {
      "id": "event.open.weather",
      "description": "打开华为天气应用某城市页，uri为固定值勿更改。cityCode来自于数据能力中ViewWeather出参cityCode字段，进行动态拼接，表示跳转到指定城市天气页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "",
        "bundleName": "",
        "intentName": "Weather_CityCode",
        "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
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
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition",
        "/location/districtName"
      ]
    }
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.weather",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "",
          "bundleName": "",
          "intentName": "Weather_CityCode",
          "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
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
  "artifactId": "8c70a80f-2634-4484-bc33-39edf87d82f2",
  "createdAt": 1793952266863
}
```
```designcompactdsl
["root","Layout",{"layout":"W-top-bottom","variant":"continuous"},["title","primary","details"]]
["title","SingleLineTitle",{"title":{"path":"/data/weather/location/districtName"},"fontSize":12}]
["primary","EmphasisText",{"mainText":{"path":"/data/weather/current/temperatureText"},"fontSize":18}]
["details","TextBlock",{"items":[{"label":"天气","value":{"path":"/data/weather/current/condition"}},{"label":"城市代码","value":{"path":"/data/weather/location/cityCode"}}]}]
["/data/weather/location/districtName","青浦区"]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
["/data/weather/location/cityCode","60814"]
```
```request
{
  "content": {
    "size": "2x4",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMS-AL20 7.0.0.111",
    "candidateAssetIds": [],
    "candidateEventCandidates": [
      {
        "capabilityId": "event.open.weather",
        "action": {
          "call": "clickToDeeplink",
          "args": {
            "abilityName": "",
            "bundleName": "",
            "intentName": "Weather_CityCode",
            "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
          }
        }
      }
    ],
    "bundleName": "com.huawei.genui",
    "description": "天气速览",
    "userQuery": "把那个大框框设置天气预报，显示当前天气和温度。",
    "title": "天气预报",
    "candidateDataBindings": [
      {
        "capabilityId": "ViewWeather",
        "arguments": {
          "forecastDays": 1
        },
        "writeResultTo": "/data/weather",
        "candidateOutputFields": [
          "/current/temperatureText",
          "/current/condition",
          "/location/districtName"
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
    "time": "20261101153656935"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q477-000",
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
  "size": "2x4",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMS-AL20 7.0.0.111",
  "candidateAssetIds": [],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.weather",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "",
          "bundleName": "",
          "intentName": "Weather_CityCode",
          "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
        }
      }
    }
  ],
  "bundleName": "com.huawei.genui",
  "description": "天气速览",
  "userQuery": "把那个大框框设置天气预报，显示当前天气和温度。",
  "title": "天气预报",
  "candidateDataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition",
        "/location/districtName"
      ]
    }
  ]
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"title\",\"primary\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":{\"path\":\"/data/weather/location/districtName\"},\"fontSize\":12}]\n[\"primary\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/weather/current/temperatureText\"},\"secondaryText\":{\"path\":\"/data/weather/current/condition\"},\"fontSize\":18}]\n[\"/data/weather/location/districtName\",\"青浦区\"]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]\n[\"/data/weather/location/cityCode\",\"60814\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "语义布局不符合合同：节点 primary：details 槽必须使用 TextBlock、TopTextBottomValue、SummaryList 或 EventCard。请选择已登记的 Layout、Region 或 Group 变体，不要修改展开后的几何。"
    }
  ]
}
```
```repair-2
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"title\",\"primary\",\"details\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":{\"path\":\"/data/weather/location/districtName\"},\"fontSize\":12}]\n[\"primary\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/weather/current/temperatureText\"},\"fontSize\":18}]\n[\"details\",\"TextBlock\",{\"items\":[{\"label\":\"天气\",\"value\":{\"path\":\"/data/weather/current/condition\"}}]}]\n[\"/data/weather/location/districtName\",\"青浦区\"]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]\n[\"/data/weather/location/cityCode\",\"60814\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "details: TextBlock.items requires 2 to 4 entries."
    }
  ]
}
```
```repair-3
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"title\",\"primary\",\"details\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":{\"path\":\"/data/weather/location/districtName\"},\"fontSize\":12}]\n[\"primary\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/weather/current/temperatureText\"},\"fontSize\":18}]\n[\"details\",\"TextBlock\",{\"items\":[{\"label\":\"天气\",\"value\":{\"path\":\"/data/weather/current/condition\"}},{\"label\":\"地区\",\"value\":{\"path\":\"/data/weather/location/districtName\"}}]}]\n[\"/data/weather/location/districtName\",\"青浦区\"]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]\n[\"/data/weather/location/cityCode\",\"60814\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_PLAN_COVERAGE_FAILED",
      "message": "Plan fact is displayed more than once in visible DSL: 所在区县名称 (/data/weather/location/districtName); expected 1, got 2; occurrences: title (SingleLineTitle).title, details (TextBlock).items[1].value.",
      "duplicateFacts": [
        {
          "requirement": "所在区县名称",
          "dataId": "/data/weather/location/districtName",
          "expectedVisibleCount": 1,
          "actualVisibleCount": 2,
          "occurrences": [
            {
              "componentId": "title",
              "componentType": "SingleLineTitle",
              "property": "title"
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
```repair-4
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"title\",\"primary\",\"details\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":{\"path\":\"/data/weather/location/districtName\"},\"fontSize\":12}]\n[\"primary\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/weather/current/temperatureText\"},\"fontSize\":18}]\n[\"details\",\"TextBlock\",{\"items\":[{\"label\":\"天气\",\"value\":{\"path\":\"/data/weather/current/condition\"}},{\"label\":\"温度\",\"value\":{\"path\":\"/data/weather/current/temperatureText\"}}]}]\n[\"/data/weather/location/districtName\",\"青浦区\"]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]\n[\"/data/weather/location/cityCode\",\"60814\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_PLAN_COVERAGE_FAILED",
      "message": "Plan fact is displayed more than once in visible DSL: 当前温度文本（已含℃单位） (/data/weather/current/temperatureText); expected 1, got 2; occurrences: primary (EmphasisText).mainText, details (TextBlock).items[1].value.",
      "duplicateFacts": [
        {
          "requirement": "当前温度文本（已含℃单位）",
          "dataId": "/data/weather/current/temperatureText",
          "expectedVisibleCount": 1,
          "actualVisibleCount": 2,
          "occurrences": [
            {
              "componentId": "primary",
              "componentType": "EmphasisText",
              "property": "mainText"
            },
            {
              "componentId": "details",
              "componentType": "TextBlock",
              "property": "items[1].value"
            }
          ],
          "ownershipInstruction": "按同一 dataId 选择唯一完整展示落点，保留已有对象标签、单位、绑定和动作；不得按相同样值去重，不得删除独有事实或造新事实填槽。若requiredDisplayPositions确认同一事实占据至少两个不同必填展示槽，不能清空属性、删除固定槽或放入占位文字；仅在repairStrategy允许范围内重新分配已有独立事实或调整必要父布局的合法组合，并补齐全部角色后完整复检。普通重复保持信息组内修复，不据此扩大为整卡重建。",
          "requiredDisplayPositions": [
            {
              "componentId": "primary",
              "componentType": "EmphasisText",
              "property": "mainText"
            }
          ]
        }
      ]
    }
  ]
}
```
```repair-5
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"title\",\"primary\",\"details\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":{\"path\":\"/data/weather/location/districtName\"},\"fontSize\":12}]\n[\"primary\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/weather/current/temperatureText\"},\"fontSize\":18}]\n[\"details\",\"TextBlock\",{\"items\":[{\"label\":\"天气\",\"value\":{\"path\":\"/data/weather/current/condition\"}},{\"label\":\"城市代码\",\"value\":{\"path\":\"/data/weather/location/cityCode\"}}]}]\n[\"/data/weather/location/districtName\",\"青浦区\"]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]\n[\"/data/weather/location/cityCode\",\"60814\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"title\",\"__layout__root__body\"],\"itemMargin\":6,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"start\",\"justifyContent\":\"start\"}},{\"id\":\"title\",\"component\":\"Row\",\"children\":[\"title_title\"],\"styles\":{\"width\":\"matchParent\",\"height\":12,\"flexShrink\":0,\"justifyContent\":\"start\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"title_title\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/location/districtName} }}\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":0,\"width\":\"matchParent\",\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"__layout__root__body\",\"component\":\"Column\",\"children\":[\"__layout__root__primary\",\"__layout__root__details\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1}},{\"id\":\"__layout__root__primary\",\"component\":\"Column\",\"children\":[\"primary\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"primary\",\"component\":\"Column\",\"children\":[\"primary_main\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"primary_main\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/temperatureText} }}\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"__layout__root__details\",\"component\":\"Column\",\"children\":[\"details\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"details\",\"component\":\"Row\",\"children\":[\"details_item0\",\"details_item1\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"alignItems\":\"top\",\"justifyContent\":\"start\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minHeight\":48}}},{\"id\":\"details_item0\",\"component\":\"Column\",\"children\":[\"details_item0_label_slot\",\"details_item0_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item0_label_slot\",\"component\":\"Row\",\"children\":[\"details_item0_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item0_label\",\"component\":\"Text\",\"content\":\"天气\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item0_value_slot\",\"component\":\"Row\",\"children\":[\"details_item0_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item0_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/condition} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"details_item1\",\"component\":\"Column\",\"children\":[\"details_item1_label_slot\",\"details_item1_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item1_label_slot\",\"component\":\"Row\",\"children\":[\"details_item1_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item1_label\",\"component\":\"Text\",\"content\":\"城市代码\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item1_value_slot\",\"component\":\"Row\",\"children\":[\"details_item1_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item1_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/location/cityCode} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"weather\":{\"location\":{\"districtName\":\"青浦区\",\"cityCode\":\"60814\"},\"current\":{\"temperatureText\":\"29℃\",\"condition\":\"多云\"}}}}}}",
  "validationErrors": []
}
```
