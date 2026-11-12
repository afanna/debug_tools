```cardspec
{
  "title": "异常天气关怀",
  "description": "天气预警与家人关怀",
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
        "forecastDays": 3
      },
      "writeResultTo": "/data/weather"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Row","children":["content","__layout__root__slots"],"itemMargin":12,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"content","component":"Column","children":["__layout__content__sub"],"styles":{"height":"matchParent","layoutWeight":1},"itemMargin":0},{"id":"__layout__content__sub","component":"Column","children":["content_title","__layout__content__body"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":126.0}},{"id":"content_title","component":"Row","children":["content_title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"content_title_title","component":"Text","content":"异常天气关怀","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__content__body","component":"Column","children":["__layout__content__primary","__layout__content__details"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__content__primary","component":"Column","children":["content_primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"content_primary","component":"Column","children":["content_primary_main","content_primary_secondary"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"content_primary_main","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"content_primary_secondary","component":"Text","content":"{{ ${/data/weather/current/condition} }}","styles":{"height":16,"fontSize":12,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__content__details","component":"Column","children":["content_support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"content_support","component":"Column","children":["content_support_row0","content_support_row1","content_support_row2"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"content_support_item0_label","component":"Text","content":"预警","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"content_support_item0_value","component":"Text","content":"{{ ${/data/weather/current/alertLevel} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"content_support_item0","component":"Row","children":["content_support_item0_label","content_support_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"content_support_row0","component":"Row","children":["content_support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"start","flexShrink":0}},{"id":"content_support_item1_label","component":"Text","content":"今日","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"content_support_item1_value","component":"Text","content":"{{ ${/data/weather/daily/0/temperatureRangeText} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"content_support_item1","component":"Row","children":["content_support_item1_label","content_support_item1_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"content_support_row1","component":"Row","children":["content_support_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"start","flexShrink":0}},{"id":"content_support_item2_value","component":"Text","content":"家人王苏东的电话号码为15251852906","styles":{"height":24.0,"fontSize":12,"fontWeight":400,"maxLines":2,"flexShrink":1,"lineHeight":1,"fontColor":"#991F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"content_support_item2","component":"Row","children":["content_support_item2_value"],"itemMargin":0,"styles":{"height":24.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"content_support_row2","component":"Row","children":["content_support_item2"],"itemMargin":0,"styles":{"width":"matchParent","height":24.0,"alignItems":"start","flexShrink":0}},{"id":"__layout__root__slots","component":"Column","children":["upper_region_shell","lower_region_shell"],"itemMargin":12,"styles":{"height":"matchParent","layoutWeight":1}},{"id":"upper","component":"Column","children":["upper_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","height":"matchParent","backgroundColor":"#99FFFFFF"}},{"id":"upper_text","component":"Column","children":["upper_primary","upper_secondary"],"itemMargin":2,"styles":{"alignItems":"start","justifyContent":"start","flexShrink":1,"constraintSize":{"minWidth":0},"height":"matchParent","padding":{"top":8},"width":"matchParent"}},{"id":"upper_primary","component":"Text","content":"王苏东","styles":{"height":19,"fontSize":14,"fontWeight":700,"maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","lineHeight":1.3571428571428572,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"upper_secondary","component":"Text","content":"家人","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","lineHeight":1.3333333333333333,"fontColor":"#991F4799"}},{"id":"lower","component":"Row","children":["lower_label","lower_visual"],"itemMargin":8,"onClick":[{"call":"clickToApi","args":{"intentName":"CallPhone","params":{"phoneNumber":"15251852906"}}}],"styles":{"width":"matchParent","height":"matchParent","padding":{"left":12,"right":12,"top":7,"bottom":7},"borderRadius":16,"backgroundColor":"#99FFFFFF","alignItems":"center","justifyContent":"spaceBetween","flexShrink":0,"constraintSize":{"minWidth":0,"minHeight":48}}},{"id":"lower_label","component":"Text","content":"拨打家人","styles":{"height":20,"fontSize":14,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1,"fontColor":"#FF1F4799"}},{"id":"lower_visual","component":"Image","src":"resources/base/media/ic_call_bule.svg","styles":{"width":24,"height":24,"objectFit":"contain","flexShrink":0}},{"id":"upper_region_shell","component":"Column","children":["upper"],"itemMargin":0,"styles":{"layoutWeight":57.0,"width":"matchParent","alignItems":"start","justifyContent":"start"}},{"id":"lower_region_shell","component":"Column","children":["lower"],"itemMargin":0,"styles":{"layoutWeight":57.0,"width":"matchParent","alignItems":"start","justifyContent":"start"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"weather":{"current":{"temperatureText":"29℃","condition":"多云","alertLevel":"大风蓝色预警"},"daily":[{"temperatureRangeText":"25℃ / 32℃"}]}},"state":{"ready":true}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "生成一个异常天气家人关怀提醒卡片，显示天气和温度变化，具备天气预警功能，有一个可以直接联系家人的电话按钮。家人电话号码绑定王苏东，手机号码15251852906。本轮卡片静态内容（用作展示的外部事实）：家人王苏东的电话号码为15251852906。",
  "size": "2x4",
  "appVersion": "11.7.8.372",
  "eventCandidates": [
    {
      "id": "event.call.phone",
      "description": "点击跳转至华为电话应用中指定号码的拨号界面。",
      "call": "clickToApi",
      "args": {
        "intentName": "CallPhone",
        "params": {
          "phoneNumber": "15251852906"
        }
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
          },
          "alertLevel": {
            "type": "string",
            "description": "预警信息。当前气象预警信息，例如'暴雨橙色预警'、'高温黄色预警'、'台风蓝色预警'。无预警时为空字符串。",
            "sampleValue": "大风蓝色预警"
          }
        },
        "daily": [
          {
            "temperatureRangeText": {
              "type": "string",
              "description": "可直接显示的最低温与最高温范围文本，每个温度值均已包含“℃”单位；展示时不得再次追加温度单位。例如“25℃ / 32℃”。",
              "sampleValue": "25℃ / 32℃"
            },
            "condition": {
              "type": "string",
              "description": "白天天气现象，来源于weather_icon。",
              "sampleValue": "多云"
            }
          },
          {
            "temperatureRangeText": {
              "type": "string",
              "description": "可直接显示的最低温与最高温范围文本，每个温度值均已包含“℃”单位；展示时不得再次追加温度单位。例如“25℃ / 32℃”。",
              "sampleValue": "25℃ / 32℃"
            },
            "condition": {
              "type": "string",
              "description": "白天天气现象，来源于weather_icon。",
              "sampleValue": "多云"
            }
          },
          {
            "temperatureRangeText": {
              "type": "string",
              "description": "可直接显示的最低温与最高温范围文本，每个温度值均已包含“℃”单位；展示时不得再次追加温度单位。例如“25℃ / 32℃”。",
              "sampleValue": "25℃ / 32℃"
            },
            "condition": {
              "type": "string",
              "description": "白天天气现象，来源于weather_icon。",
              "sampleValue": "多云"
            }
          }
        ]
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.ic_weatherWarning",
      "src": "resources/base/media/ic_weatherWarning.svg",
      "description": "样式：浅灰渐变云朵内带深色感叹号的天气预警图标，原始尺寸为 24×24，SVG 矢量图（保留原色，禁止染色）保留渐变配色；适用：天气卡片中的气象预警提示，可结合 ViewWeather 输出的 alertLevel 字段展示，也可作为天气预警详情入口的辅助图标。不表示所有天气变化或空气质量异常；无预警时不应显示该图标，也不替代具体预警等级文案。"
    },
    {
      "id": "asset.ic_call_bule",
      "src": "resources/base/media/ic_call_bule.svg",
      "description": "样式：蓝色纵向渐变圆形底上的白色电话听筒图标，原始尺寸为 20×20，SVG 矢量图（保留原色，禁止染色）需保留原始渐变配色，禁止染色；适用：拨号、联系人呼叫或电话快捷操作卡片，可配合 event.call.phone 跳转到指定号码的拨号界面。图标不表示正在通话、来电或联系人身份。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "ViewWeather"
  ],
  "event": [
    {
      "id": "event.call.phone",
      "description": "点击跳转至华为电话应用中指定号码的拨号界面。",
      "call": "clickToApi",
      "args": {
        "intentName": "CallPhone",
        "params": {
          "phoneNumber": "15251852906"
        }
      }
    }
  ],
  "asset": [
    "asset.ic_weatherWarning",
    "asset.ic_call_bule"
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
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 3
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition",
        "/current/alertLevel",
        "/daily/0/temperatureRangeText",
        "/daily/1/temperatureRangeText",
        "/daily/2/temperatureRangeText",
        "/daily/0/condition",
        "/daily/1/condition",
        "/daily/2/condition"
      ]
    }
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.call.phone",
      "action": {
        "call": "clickToApi",
        "args": {
          "intentName": "CallPhone",
          "params": {
            "phoneNumber": "15251852906"
          }
        }
      }
    }
  ],
  "candidateAssetIds": [
    "asset.ic_weatherWarning",
    "asset.ic_call_bule"
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
  "artifactId": "ad996729-7674-4e95-9dd7-20dc921e8991",
  "createdAt": 1793934583936
}
```
```designcompactdsl
["root","Layout",{"layout":"W-content-side-slots","orientation":"content-left"},["content","upper","lower"]]
["content","Region",{"variant":"title-hero-support"},["content_title","content_primary","content_support"]]
["content_title","SingleLineTitle",{"title":"异常天气关怀","fontSize":12}]
["content_primary","EmphasisText",{"mainText":{"path":"/data/weather/current/temperatureText"},"secondaryText":{"path":"/data/weather/current/condition"},"fontSize":18}]
["content_support","SecondaryBody",{"columns":1,"items":[{"label":"预警 ","value":{"path":"/data/weather/current/alertLevel"}},{"label":"今日 ","value":{"path":"/data/weather/daily/0/temperatureRangeText"}},{"value":"家人王苏东的电话号码为15251852906","maxLines":2}],"fontSize":12}]
["upper","InfoBlock",{"variant":"slot","primaryText":"王苏东","secondaryText":"家人","surfaceRole":"panel"}]
["lower","CardButton",{"label":"拨打家人","icon":"resources/base/media/ic_call_bule.svg","onClick":[{"call":"clickToApi","args":{"intentName":"CallPhone","params":{"phoneNumber":"15251852906"}}}]}]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
["/data/weather/current/alertLevel","大风蓝色预警"]
["/data/weather/daily/0/temperatureRangeText","25℃ / 32℃"]
["/state/ready",true]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "生成一个异常天气家人关怀提醒卡片，显示天气和温度变化，具备天气预警功能，有一个可以直接联系家人的电话按钮。家人电话号码绑定王苏东，手机号码15251852906。本轮卡片静态内容（用作展示的外部事实）：家人王苏东的电话号码为15251852906。",
    "candidateDataBindings": [
      {
        "capabilityId": "ViewWeather",
        "arguments": {
          "forecastDays": 3
        },
        "writeResultTo": "/data/weather",
        "candidateOutputFields": [
          "/current/temperatureText",
          "/current/condition",
          "/current/alertLevel",
          "/daily/0/temperatureRangeText",
          "/daily/1/temperatureRangeText",
          "/daily/2/temperatureRangeText",
          "/daily/0/condition",
          "/daily/1/condition",
          "/daily/2/condition"
        ]
      }
    ],
    "title": "异常天气关怀",
    "size": "2x4",
    "candidateEventCandidates": [
      {
        "capabilityId": "event.call.phone",
        "action": {
          "call": "clickToApi",
          "args": {
            "intentName": "CallPhone",
            "params": {
              "phoneNumber": "15251852906"
            }
          }
        }
      }
    ],
    "description": "天气预警与家人关怀",
    "candidateAssetIds": [
      "asset.ic_weatherWarning",
      "asset.ic_call_bule"
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "DPX-AL00",
    "prdVer": "11.7.8.372",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261030081433585"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q345-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "生成一个异常天气家人关怀提醒卡片，显示天气和温度变化，具备天气预警功能，有一个可以直接联系家人的电话按钮。家人电话号码绑定王苏东，手机号码15251852906。本轮卡片静态内容（用作展示的外部事实）：家人王苏东的电话号码为15251852906。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "DPX-AL00 6.0.0.120",
  "bundleName": "com.huawei.genui",
  "userQuery": "生成一个异常天气家人关怀提醒卡片，显示天气和温度变化，具备天气预警功能，有一个可以直接联系家人的电话按钮。家人电话号码绑定王苏东，手机号码15251852906。本轮卡片静态内容（用作展示的外部事实）：家人王苏东的电话号码为15251852906。",
  "candidateDataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 3
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition",
        "/current/alertLevel",
        "/daily/0/temperatureRangeText",
        "/daily/1/temperatureRangeText",
        "/daily/2/temperatureRangeText",
        "/daily/0/condition",
        "/daily/1/condition",
        "/daily/2/condition"
      ]
    }
  ],
  "title": "异常天气关怀",
  "size": "2x4",
  "candidateEventCandidates": [
    {
      "capabilityId": "event.call.phone",
      "action": {
        "call": "clickToApi",
        "args": {
          "intentName": "CallPhone",
          "params": {
            "phoneNumber": "15251852906"
          }
        }
      }
    }
  ],
  "description": "天气预警与家人关怀",
  "candidateAssetIds": [
    "asset.ic_weatherWarning",
    "asset.ic_call_bule"
  ]
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-content-side-slots\",\"orientation\":\"content-left\"},[\"content\",\"upper\",\"lower\"]]\n[\"content_title\",\"SingleLineTitle\",{\"title\":\"异常天气关怀\",\"icon\":\"resources/base/media/ic_weatherWarning.svg\",\"fontSize\":12}]\n[\"content_primary\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/weather/current/temperatureText\"},\"secondaryText\":{\"path\":\"/data/weather/current/condition\"},\"fontSize\":18}]\n[\"content_support\",\"SecondaryBody\",{\"columns\":1,\"items\":[{\"label\":\"预警 \",\"value\":{\"path\":\"/data/weather/current/alertLevel\"}},{\"label\":\"今日 \",\"value\":{\"path\":\"/data/weather/daily/0/temperatureRangeText\"}},{\"value\":\"家人王苏东的电话号码为15251852906\",\"maxLines\":2}],\"fontSize\":12}]\n[\"content\",\"Region\",{\"variant\":\"title-hero-support\"},[\"content_title\",\"content_primary\",\"content_support\"]]\n[\"upper\",\"InfoBlock\",{\"variant\":\"slot\",\"primaryText\":\"王苏东\",\"secondaryText\":\"家人\",\"surfaceRole\":\"panel\"}]\n[\"lower\",\"CardButton\",{\"label\":\"拨打家人\",\"icon\":\"resources/base/media/ic_call_bule.svg\",\"onClick\":[{\"call\":\"clickToApi\",\"args\":{\"intentName\":\"CallPhone\",\"params\":{\"phoneNumber\":\"15251852906\"}}}]}]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]\n[\"/data/weather/current/alertLevel\",\"大风蓝色预警\"]\n[\"/data/weather/daily/0/temperatureRangeText\",\"25℃ / 32℃\"]\n[\"/state/ready\",true]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Row\",\"children\":[\"content\",\"__layout__root__slots\"],\"itemMargin\":12,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"center\",\"justifyContent\":\"start\"}},{\"id\":\"content\",\"component\":\"Column\",\"children\":[\"__layout__content__sub\"],\"styles\":{\"height\":\"matchParent\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"__layout__content__sub\",\"component\":\"Column\",\"children\":[\"content_title\",\"__layout__content__body\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":126.0}},{\"id\":\"content_title\",\"component\":\"Row\",\"children\":[\"content_title_title\"],\"styles\":{\"width\":\"matchParent\",\"height\":12,\"flexShrink\":0,\"justifyContent\":\"start\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"content_title_title\",\"component\":\"Text\",\"content\":\"异常天气关怀\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":0,\"width\":\"matchParent\",\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"__layout__content__body\",\"component\":\"Column\",\"children\":[\"__layout__content__primary\",\"__layout__content__details\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1}},{\"id\":\"__layout__content__primary\",\"component\":\"Column\",\"children\":[\"content_primary\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"content_primary\",\"component\":\"Column\",\"children\":[\"content_primary_main\",\"content_primary_secondary\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"content_primary_main\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/temperatureText} }}\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"content_primary_secondary\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/condition} }}\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1.3333333333333333,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"__layout__content__details\",\"component\":\"Column\",\"children\":[\"content_support\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"content_support\",\"component\":\"Column\",\"children\":[\"content_support_row0\",\"content_support_row1\",\"content_support_row2\"],\"itemMargin\":2,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"flexShrink\":1}},{\"id\":\"content_support_item0_label\",\"component\":\"Text\",\"content\":\"预警\",\"styles\":{\"height\":12,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":0,\"lineHeight\":1,\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"clip\"}},{\"id\":\"content_support_item0_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/alertLevel} }}\",\"styles\":{\"height\":12.0,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/1\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"content_support_item0\",\"component\":\"Row\",\"children\":[\"content_support_item0_label\",\"content_support_item0_value\"],\"itemMargin\":4,\"styles\":{\"height\":12.0,\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"content_support_row0\",\"component\":\"Row\",\"children\":[\"content_support_item0\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":12.0,\"alignItems\":\"start\",\"flexShrink\":0}},{\"id\":\"content_support_item1_label\",\"component\":\"Text\",\"content\":\"今日\",\"styles\":{\"height\":12,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":0,\"lineHeight\":1,\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"clip\"}},{\"id\":\"content_support_item1_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/daily/0/temperatureRangeText} }}\",\"styles\":{\"height\":12.0,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/1\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"content_support_item1\",\"component\":\"Row\",\"children\":[\"content_support_item1_label\",\"content_support_item1_value\"],\"itemMargin\":4,\"styles\":{\"height\":12.0,\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"content_support_row1\",\"component\":\"Row\",\"children\":[\"content_support_item1\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":12.0,\"alignItems\":\"start\",\"flexShrink\":0}},{\"id\":\"content_support_item2_value\",\"component\":\"Text\",\"content\":\"家人王苏东的电话号码为15251852906\",\"styles\":{\"height\":24.0,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":2,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/0.6\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"content_support_item2\",\"component\":\"Row\",\"children\":[\"content_support_item2_value\"],\"itemMargin\":0,\"styles\":{\"height\":24.0,\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"content_support_row2\",\"component\":\"Row\",\"children\":[\"content_support_item2\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":24.0,\"alignItems\":\"start\",\"flexShrink\":0}},{\"id\":\"__layout__root__slots\",\"component\":\"Column\",\"children\":[\"upper_region_shell\",\"lower_region_shell\"],\"itemMargin\":12,\"styles\":{\"height\":\"matchParent\",\"layoutWeight\":1}},{\"id\":\"upper\",\"component\":\"Column\",\"children\":[\"upper_text\"],\"itemMargin\":0,\"styles\":{\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"clip\":true,\"flexShrink\":0,\"width\":\"matchParent\",\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\"}},{\"id\":\"upper_text\",\"component\":\"Column\",\"children\":[\"upper_primary\",\"upper_secondary\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"height\":\"matchParent\",\"padding\":{\"top\":8},\"width\":\"matchParent\"}},{\"id\":\"upper_primary\",\"component\":\"Text\",\"content\":\"王苏东\",\"styles\":{\"height\":19,\"fontSize\":14,\"fontWeight\":700,\"maxLines\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\",\"lineHeight\":1.3571428571428572,\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"upper_secondary\",\"component\":\"Text\",\"content\":\"家人\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":500,\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\",\"lineHeight\":1.3333333333333333,\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"lower\",\"component\":\"Row\",\"children\":[\"lower_label\",\"lower_visual\"],\"itemMargin\":8,\"onClick\":[{\"call\":\"clickToApi\",\"args\":{\"intentName\":\"CallPhone\",\"params\":{\"phoneNumber\":\"15251852906\"}}}],\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":{\"left\":12,\"right\":12,\"top\":7,\"bottom\":7},\"borderRadius\":16,\"backgroundColor\":\"@theme:panel/1\",\"alignItems\":\"center\",\"justifyContent\":\"spaceBetween\",\"flexShrink\":0,\"constraintSize\":{\"minWidth\":0,\"minHeight\":48}}},{\"id\":\"lower_label\",\"component\":\"Text\",\"content\":\"拨打家人\",\"styles\":{\"height\":20,\"fontSize\":14,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1,\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"lower_visual\",\"component\":\"Image\",\"src\":\"resources/base/media/ic_call_bule.svg\",\"styles\":{\"width\":24,\"height\":24,\"objectFit\":\"contain\",\"flexShrink\":0}},{\"id\":\"upper_region_shell\",\"component\":\"Column\",\"children\":[\"upper\"],\"itemMargin\":0,\"styles\":{\"layoutWeight\":57.0,\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\"}},{\"id\":\"lower_region_shell\",\"component\":\"Column\",\"children\":[\"lower\"],\"itemMargin\":0,\"styles\":{\"layoutWeight\":57.0,\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"weather\":{\"current\":{\"temperatureText\":\"29℃\",\"condition\":\"多云\",\"alertLevel\":\"大风蓝色预警\"},\"daily\":[{\"temperatureRangeText\":\"25℃ / 32℃\"}]}},\"state\":{\"ready\":true}}}}",
  "validationErrors": []
}
```
