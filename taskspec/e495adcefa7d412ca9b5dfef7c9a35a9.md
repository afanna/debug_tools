```cardspec
{
  "title": "穿戴健康",
  "description": "运动健康数据卡片",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetHealthAndSportSummary",
      "arguments": {
        "targetDayOffset": 0
      },
      "writeResultTo": "/data/health"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Stack","children":["fusionBallBackground","__genui_render_component__root"],"styles":{"width":"matchParent","height":"matchParent","padding":0,"borderRadius":20,"clip":true,"backgroundColor":"#00000000","alignContent":"topStart"}},{"id":"fusionBallBackground","component":"Stack","children":["fusionBallLargeSlot","fusionBallMediumSlot","fusionBallSmallSlot","fusionBallGlassLayer"],"styles":{"width":"100%","height":"100%","borderRadius":20,"alignContent":"topStart","clip":true}},{"id":"fusionBallLargeSlot","component":"Stack","children":["fusionBallLarge"],"styles":{"width":"112.5%","height":"27.5%","alignContent":"center"}},{"id":"fusionBallLarge","component":"Divider","styles":{"width":"116.666667%","height":"477.272727%","strokeWidth":0,"color":"#00000000","borderRadius":105,"backgroundColor":"#FFF24131","clip":true}},{"id":"fusionBallMediumSlot","component":"Stack","children":["fusionBallMedium"],"styles":{"width":"50%","height":"137.5%","alignContent":"bottom"}},{"id":"fusionBallMedium","component":"Divider","styles":{"width":"200%","height":"72.727273%","strokeWidth":0,"color":"#00000000","borderRadius":80,"backgroundColor":"#FFFF8833","clip":true}},{"id":"fusionBallSmallSlot","component":"Stack","children":["fusionBallSmall"],"styles":{"width":"121.875%","height":"118.75%","alignContent":"bottomEnd"}},{"id":"fusionBallSmall","component":"Divider","styles":{"width":"51.282051%","height":"52.631579%","strokeWidth":0,"color":"#00000000","borderRadius":50,"backgroundColor":"#FFE68073","clip":true}},{"id":"fusionBallGlassLayer","component":"Divider","styles":{"width":"100%","height":"100%","strokeWidth":0,"color":"#00000000","backgroundColor":"#0DFFFFFF","backdropBlur":{"radius":210}}},{"id":"__genui_render_component__root","component":"Column","children":["title_area","content_area"],"itemMargin":4,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"start"}},{"id":"title_area","component":"Row","children":["title_area_title"],"itemMargin":0,"styles":{"width":126,"height":20,"flexShrink":0,"justifyContent":"start","alignItems":"center"}},{"id":"title_area_title","component":"Text","content":"运动健康","styles":{"width":126,"fontSize":12,"fontWeight":400,"fontColor":"#FFFFFFFF","textAlign":"start","maxLines":1,"flexShrink":0}},{"id":"content_area","component":"Column","children":["metrics_row","sleep_info"],"itemMargin":8,"styles":{"width":126,"layoutWeight":1,"justifyContent":"center","alignItems":"start","flexShrink":1}},{"id":"metrics_row","component":"Row","children":["steps_col","calories_col"],"styles":{"width":126,"justifyContent":"spaceBetween","alignItems":"center","flexShrink":0}},{"id":"steps_col","component":"Column","children":["steps_value","steps_label"],"itemMargin":2,"styles":{"width":58,"justifyContent":"center","alignItems":"center","flexShrink":0}},{"id":"steps_value","component":"Text","content":"{{ ${/data/health/dailySteps} + '步' }}","styles":{"fontSize":18,"fontWeight":700,"fontColor":"#FFFFFFFF","maxLines":1,"textOverflow":"clip"}},{"id":"steps_label","component":"Text","content":"步数","styles":{"fontSize":12,"fontWeight":400,"fontColor":"#FFFFFFFF","maxLines":1,"textOverflow":"clip"}},{"id":"calories_col","component":"Column","children":["calories_value","calories_label"],"itemMargin":2,"styles":{"width":58,"justifyContent":"center","alignItems":"center","flexShrink":0}},{"id":"calories_value","component":"Text","content":"{{ ${/data/health/dailyTotalCaloriesText} }}","styles":{"fontSize":18,"fontWeight":700,"fontColor":"#FFFFFFFF","maxLines":1,"textOverflow":"clip"}},{"id":"calories_label","component":"Text","content":"热量","styles":{"fontSize":12,"fontWeight":400,"fontColor":"#FFFFFFFF","maxLines":1,"textOverflow":"clip"}},{"id":"sleep_info","component":"Row","children":["sleep_dot","sleep_text"],"itemMargin":6,"styles":{"width":126,"justifyContent":"start","alignItems":"center","flexShrink":0}},{"id":"sleep_dot","component":"Image","src":"resources/base/media/moon_z_fill_1.svg","styles":{"width":20,"height":20,"objectFit":"contain","fillColor":"#FFFFFFFF","flexShrink":0}},{"id":"sleep_text","component":"Text","content":"{{ '睡眠 ' + ${/data/health/sleepScore} + '分 ' + ${/data/health/sleepStatus} }}","styles":{"fontSize":12,"fontWeight":400,"fontColor":"#FFFFFFFF","maxLines":1,"textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"health":{"dailySteps":6200,"dailyTotalCaloriesText":"420 千卡","sleepScore":82,"sleepStatus":"良好","nightSleepDurationText":"7小时1分"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "打开穿戴卡，展示运动健康数据（步数、热量、距离、睡眠等）",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "health": {
        "dailySteps": {
          "type": "integer",
          "description": "与最新睡眠同属一天的日常全天累计活动总步数纯整数，返回值不包含“步”。若直接用于文本展示，必须在数值后追加“步”。",
          "sampleValue": 6200
        },
        "dailyTotalCaloriesText": {
          "type": "string",
          "description": "可直接显示的日常活动总消耗热量文本，已完成千分位归一化并包含“千卡”单位；展示时不得再次追加热量单位。例如“998 千卡”。",
          "sampleValue": "420 千卡"
        },
        "dailyDistanceText": {
          "type": "string",
          "description": "可直接显示的日常活动总距离文本，端侧已根据数值大小换算并包含“米”或“公里”单位；展示时不得再次追加距离单位。例如“5.42 公里”或“755 米”。",
          "sampleValue": "4.60 公里"
        },
        "sleepScore": {
          "type": "integer",
          "description": "睡眠综合得分，取值范围 0-100。",
          "sampleValue": 82
        },
        "sleepStatus": {
          "type": "string",
          "description": "基于得分智能生成的睡眠状态语义判定，包括：'优秀'、'良好'、'一般'、'较差'。",
          "sampleValue": "良好"
        },
        "nightSleepDurationText": {
          "type": "string",
          "description": "可直接显示的夜间正式睡眠总时长文本，已包含“小时”或“分”等时间单位；展示时不得再次追加时间单位。例如“7小时1分”。",
          "sampleValue": "7小时1分"
        }
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.emoji_Fitness_Health",
      "src": "resources/base/media/emoji_Fitness_Health.png",
      "description": "样式：橙色方形底上的白色运动健康应用标识，不透明背景，原始尺寸为 1024×1024，PNG 位图保留原色；适用：运动健康应用、健身记录或活动目标相关卡片。"
    },
    {
      "id": "asset.figure_run",
      "src": "resources/base/media/figure_run.svg",
      "description": "样式：跑步人物图标，默认黑色，图形为人体奔跑动作侧视轮廓；适用：运动记录、跑步锻炼追踪、步数统计。"
    },
    {
      "id": "asset.flame_fill",
      "src": "resources/base/media/flame_fill.svg",
      "description": "样式：默认黑色的单色实心火焰图标；适用：运动热量消耗、燃烧、火焰或加热状态。"
    },
    {
      "id": "asset.moon_z_fill_1",
      "src": "resources/base/media/moon_z_fill_1.svg",
      "description": "样式：月亮加Z睡眠实心图标，默认黑色，图形为月牙旁附带字母Z表示入睡；适用：睡眠模式开启、休息提醒、晚安场景。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "GetHealthAndSportSummary"
  ],
  "event": [],
  "asset": [
    "asset.emoji_Fitness_Health",
    "asset.figure_run",
    "asset.flame_fill",
    "asset.moon_z_fill_1"
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
      "capabilityId": "GetHealthAndSportSummary",
      "arguments": {
        "targetDayOffset": 0
      },
      "writeResultTo": "/data/health",
      "candidateOutputFields": [
        "/dailySteps",
        "/dailyTotalCaloriesText",
        "/dailyDistanceText",
        "/sleepScore",
        "/sleepStatus",
        "/nightSleepDurationText"
      ]
    }
  ],
  "candidateEventCandidates": [],
  "candidateAssetIds": [
    "asset.emoji_Fitness_Health",
    "asset.figure_run",
    "asset.flame_fill",
    "asset.moon_z_fill_1"
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
  "artifactId": "32fb188f-a85f-42fb-b41e-c8f320995255",
  "createdAt": 1793685404383
}
```
```designcompactdsl
["root","Column",{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"start","itemMargin":4,"design":"fusion-ball-sport-orange"},["title_area","content_area"]]
["title_area","CardHeader",{"title":"运动健康","fontColor":"#FFFFFFFF"}]
["content_area","Column",{"width":126,"layoutWeight":1,"justifyContent":"center","alignItems":"start","itemMargin":8,"flexShrink":1},["metrics_row","sleep_info"]]
["metrics_row","Row",{"width":126,"justifyContent":"spaceBetween","alignItems":"center","flexShrink":0},["steps_col","calories_col"]]
["steps_col","Column",{"width":58,"justifyContent":"center","alignItems":"center","itemMargin":2,"flexShrink":0},["steps_value","steps_label"]]
["steps_value","Text",{"content":"{{ ${/data/health/dailySteps} + '步' }}","fontSize":18,"fontWeight":700,"fontColor":"#FFFFFFFF","maxLines":1}]
["steps_label","Text",{"content":"步数","fontSize":12,"fontWeight":400,"fontColor":"#CCFFFFFF","maxLines":1}]
["calories_col","Column",{"width":58,"justifyContent":"center","alignItems":"center","itemMargin":2,"flexShrink":0},["calories_value","calories_label"]]
["calories_value","Text",{"content":{"path":"/data/health/dailyTotalCaloriesText"},"fontSize":18,"fontWeight":700,"fontColor":"#FFFFFFFF","maxLines":1}]
["calories_label","Text",{"content":"热量","fontSize":12,"fontWeight":400,"fontColor":"#CCFFFFFF","maxLines":1}]
["sleep_info","Row",{"width":126,"justifyContent":"start","alignItems":"center","itemMargin":6,"flexShrink":0},["sleep_dot","sleep_text"]]
["sleep_dot","Image",{"src":"resources/base/media/moon_z_fill_1.svg","width":20,"height":20,"objectFit":"contain","fillColor":"#CCFFFFFF","flexShrink":0}]
["sleep_text","Text",{"content":"{{ '睡眠 ' + ${/data/health/sleepScore} + '分 ' + ${/data/health/sleepStatus} }}","fontSize":12,"fontWeight":400,"fontColor":"#FFFFFFFF","maxLines":1}]
["/data/health/dailySteps",6200]
["/data/health/dailyTotalCaloriesText","420 千卡"]
["/data/health/sleepScore",82]
["/data/health/sleepStatus","良好"]
["/data/health/nightSleepDurationText","7小时1分"]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMM-AL10P 7.0.0.111",
    "candidateAssetIds": [
      "asset.emoji_Fitness_Health",
      "asset.figure_run",
      "asset.flame_fill",
      "asset.moon_z_fill_1"
    ],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "运动健康数据卡片",
    "userQuery": "打开穿戴卡，展示运动健康数据（步数、热量、距离、睡眠等）",
    "title": "穿戴健康",
    "candidateDataBindings": [
      {
        "arguments": {
          "targetDayOffset": 0
        },
        "candidateOutputFields": [
          "/dailySteps",
          "/dailyTotalCaloriesText",
          "/dailyDistanceText",
          "/sleepScore",
          "/sleepStatus",
          "/nightSleepDurationText"
        ],
        "capabilityId": "GetHealthAndSportSummary",
        "writeResultTo": "/data/health"
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
    "time": "20261103055620500"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "1",
    "isNew": false,
    "sessionId": "4331d8a2-3d51-458a-9520-1d0a7004e43b"
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
    "asset.emoji_Fitness_Health",
    "asset.figure_run",
    "asset.flame_fill",
    "asset.moon_z_fill_1"
  ],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "运动健康数据卡片",
  "userQuery": "打开穿戴卡，展示运动健康数据（步数、热量、距离、睡眠等）",
  "title": "穿戴健康",
  "candidateDataBindings": [
    {
      "arguments": {
        "targetDayOffset": 0
      },
      "candidateOutputFields": [
        "/dailySteps",
        "/dailyTotalCaloriesText",
        "/dailyDistanceText",
        "/sleepScore",
        "/sleepStatus",
        "/nightSleepDurationText"
      ],
      "capabilityId": "GetHealthAndSportSummary",
      "writeResultTo": "/data/health"
    }
  ]
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Column\",{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"itemMargin\":4,\"design\":\"fusion-ball-sport-orange\"},[\"title_area\",\"content_area\"]]\n[\"title_area\",\"CardHeader\",{\"title\":\"运动健康\",\"fontColor\":\"#FFFFFFFF\"}]\n[\"content_area\",\"Column\",{\"width\":126,\"layoutWeight\":1,\"justifyContent\":\"center\",\"alignItems\":\"start\",\"itemMargin\":8,\"flexShrink\":1},[\"metrics_row\",\"sleep_info\"]]\n[\"metrics_row\",\"Row\",{\"width\":126,\"justifyContent\":\"spaceBetween\",\"alignItems\":\"center\",\"flexShrink\":0},[\"steps_col\",\"calories_col\"]]\n[\"steps_col\",\"Column\",{\"width\":58,\"justifyContent\":\"center\",\"alignItems\":\"center\",\"itemMargin\":2,\"flexShrink\":0},[\"steps_value\",\"steps_label\"]]\n[\"steps_value\",\"Text\",{\"content\":{\"path\":\"/data/health/dailySteps\"},\"fontSize\":18,\"fontWeight\":700,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1}]\n[\"steps_label\",\"Text\",{\"content\":\"步数 · 步\",\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#CCFFFFFF\",\"maxLines\":1}]\n[\"calories_col\",\"Column\",{\"width\":58,\"justifyContent\":\"center\",\"alignItems\":\"center\",\"itemMargin\":2,\"flexShrink\":0},[\"calories_value\",\"calories_label\"]]\n[\"calories_value\",\"Text\",{\"content\":{\"path\":\"/data/health/dailyTotalCaloriesText\"},\"fontSize\":18,\"fontWeight\":700,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1}]\n[\"calories_label\",\"Text\",{\"content\":\"热量\",\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#CCFFFFFF\",\"maxLines\":1}]\n[\"sleep_info\",\"Row\",{\"width\":126,\"justifyContent\":\"start\",\"alignItems\":\"center\",\"itemMargin\":6,\"flexShrink\":0},[\"sleep_dot\",\"sleep_text\"]]\n[\"sleep_dot\",\"Image\",{\"src\":\"resources/base/media/moon_z_fill_1.svg\",\"width\":20,\"height\":20,\"objectFit\":\"contain\",\"fillColor\":\"#CCFFFFFF\",\"flexShrink\":0}]\n[\"sleep_text\",\"Text\",{\"content\":\"{{ '睡眠 ' + ${/data/health/sleepScore} + '分 ' + ${/data/health/sleepStatus} }}\",\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1}]\n[\"/data/health/dailySteps\",6200]\n[\"/data/health/dailyTotalCaloriesText\",\"420 千卡\"]\n[\"/data/health/sleepScore\",82]\n[\"/data/health/sleepStatus\",\"良好\"]\n[\"/data/health/nightSleepDurationText\",\"7小时1分\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Stack\",\"children\":[\"fusionBallBackground\",\"__genui_render_component__root\"],\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":0,\"borderRadius\":20,\"clip\":true,\"backgroundColor\":\"#00000000\",\"alignContent\":\"topStart\"}},{\"id\":\"fusionBallBackground\",\"component\":\"Stack\",\"children\":[\"fusionBallLargeSlot\",\"fusionBallMediumSlot\",\"fusionBallSmallSlot\",\"fusionBallGlassLayer\"],\"styles\":{\"width\":\"100%\",\"height\":\"100%\",\"borderRadius\":20,\"alignContent\":\"topStart\",\"clip\":true}},{\"id\":\"fusionBallLargeSlot\",\"component\":\"Stack\",\"children\":[\"fusionBallLarge\"],\"styles\":{\"width\":\"112.5%\",\"height\":\"27.5%\",\"alignContent\":\"center\"}},{\"id\":\"fusionBallLarge\",\"component\":\"Divider\",\"styles\":{\"width\":\"116.666667%\",\"height\":\"477.272727%\",\"strokeWidth\":0,\"color\":\"#00000000\",\"borderRadius\":105,\"backgroundColor\":\"#FFF24131\",\"clip\":true}},{\"id\":\"fusionBallMediumSlot\",\"component\":\"Stack\",\"children\":[\"fusionBallMedium\"],\"styles\":{\"width\":\"50%\",\"height\":\"137.5%\",\"alignContent\":\"bottom\"}},{\"id\":\"fusionBallMedium\",\"component\":\"Divider\",\"styles\":{\"width\":\"200%\",\"height\":\"72.727273%\",\"strokeWidth\":0,\"color\":\"#00000000\",\"borderRadius\":80,\"backgroundColor\":\"#FFFF8833\",\"clip\":true}},{\"id\":\"fusionBallSmallSlot\",\"component\":\"Stack\",\"children\":[\"fusionBallSmall\"],\"styles\":{\"width\":\"121.875%\",\"height\":\"118.75%\",\"alignContent\":\"bottomEnd\"}},{\"id\":\"fusionBallSmall\",\"component\":\"Divider\",\"styles\":{\"width\":\"51.282051%\",\"height\":\"52.631579%\",\"strokeWidth\":0,\"color\":\"#00000000\",\"borderRadius\":50,\"backgroundColor\":\"#FFE68073\",\"clip\":true}},{\"id\":\"fusionBallGlassLayer\",\"component\":\"Divider\",\"styles\":{\"width\":\"100%\",\"height\":\"100%\",\"strokeWidth\":0,\"color\":\"#00000000\",\"backgroundColor\":\"#0DFFFFFF\",\"backdropBlur\":{\"radius\":210}}},{\"id\":\"__genui_render_component__root\",\"component\":\"Column\",\"children\":[\"title_area\",\"content_area\"],\"itemMargin\":4,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"center\",\"justifyContent\":\"start\"}},{\"id\":\"title_area\",\"component\":\"Row\",\"children\":[\"title_area_title\"],\"itemMargin\":0,\"styles\":{\"width\":126,\"height\":20,\"flexShrink\":0,\"justifyContent\":\"start\",\"alignItems\":\"center\"}},{\"id\":\"title_area_title\",\"component\":\"Text\",\"content\":\"运动健康\",\"styles\":{\"width\":126,\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#FFFFFFFF\",\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":0}},{\"id\":\"content_area\",\"component\":\"Column\",\"children\":[\"metrics_row\",\"sleep_info\"],\"itemMargin\":8,\"styles\":{\"width\":126,\"layoutWeight\":1,\"justifyContent\":\"center\",\"alignItems\":\"start\",\"flexShrink\":1}},{\"id\":\"metrics_row\",\"component\":\"Row\",\"children\":[\"steps_col\",\"calories_col\"],\"styles\":{\"width\":126,\"justifyContent\":\"spaceBetween\",\"alignItems\":\"center\",\"flexShrink\":0}},{\"id\":\"steps_col\",\"component\":\"Column\",\"children\":[\"steps_value\",\"steps_label\"],\"itemMargin\":2,\"styles\":{\"width\":58,\"justifyContent\":\"center\",\"alignItems\":\"center\",\"flexShrink\":0}},{\"id\":\"steps_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/health/dailySteps} }}\",\"styles\":{\"fontSize\":18,\"fontWeight\":700,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1,\"textOverflow\":\"clip\"}},{\"id\":\"steps_label\",\"component\":\"Text\",\"content\":\"步数 · 步\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1,\"textOverflow\":\"clip\"}},{\"id\":\"calories_col\",\"component\":\"Column\",\"children\":[\"calories_value\",\"calories_label\"],\"itemMargin\":2,\"styles\":{\"width\":58,\"justifyContent\":\"center\",\"alignItems\":\"center\",\"flexShrink\":0}},{\"id\":\"calories_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/health/dailyTotalCaloriesText} }}\",\"styles\":{\"fontSize\":18,\"fontWeight\":700,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1,\"textOverflow\":\"clip\"}},{\"id\":\"calories_label\",\"component\":\"Text\",\"content\":\"热量\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1,\"textOverflow\":\"clip\"}},{\"id\":\"sleep_info\",\"component\":\"Row\",\"children\":[\"sleep_dot\",\"sleep_text\"],\"itemMargin\":6,\"styles\":{\"width\":126,\"justifyContent\":\"start\",\"alignItems\":\"center\",\"flexShrink\":0}},{\"id\":\"sleep_dot\",\"component\":\"Image\",\"src\":\"resources/base/media/moon_z_fill_1.svg\",\"styles\":{\"width\":20,\"height\":20,\"objectFit\":\"contain\",\"fillColor\":\"#FFFFFFFF\",\"flexShrink\":0}},{\"id\":\"sleep_text\",\"component\":\"Text\",\"content\":\"{{ '睡眠 ' + ${/data/health/sleepScore} + '分 ' + ${/data/health/sleepStatus} }}\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1,\"textOverflow\":\"clip\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"health\":{\"dailySteps\":6200,\"dailyTotalCaloriesText\":\"420 千卡\",\"sleepScore\":82,\"sleepStatus\":\"良好\",\"nightSleepDurationText\":\"7小时1分\"}}}}}",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "DISPLAY_UNIT_MISSING",
      "message": "动态数值字段不包含展示单位，当前 Text 未展示其声明的单位。",
      "category": "ARTIFACT_VALIDATION_FAILED",
      "validatorStage": "semantic",
      "fileKind": "genui",
      "line": 2,
      "jsonPointer": "/updateComponents/componentsById/steps_value/content",
      "actual": "{{ ${/data/health/dailySteps} }}",
      "expected": {
        "unitIncluded": false,
        "displayUnits": [
          "步"
        ]
      },
      "fixHint": "在数值表达式中追加单位“步”，或让紧邻数值后的静态 Text 包含该单位，且整组只展示一次。"
    }
  ]
}
```
```repair-2
{
  "modelGeneratedCompactDsl": "[\"root\",\"Column\",{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"itemMargin\":4,\"design\":\"fusion-ball-sport-orange\"},[\"title_area\",\"content_area\"]]\n[\"title_area\",\"CardHeader\",{\"title\":\"运动健康\",\"fontColor\":\"#FFFFFFFF\"}]\n[\"content_area\",\"Column\",{\"width\":126,\"layoutWeight\":1,\"justifyContent\":\"center\",\"alignItems\":\"start\",\"itemMargin\":8,\"flexShrink\":1},[\"metrics_row\",\"sleep_info\"]]\n[\"metrics_row\",\"Row\",{\"width\":126,\"justifyContent\":\"spaceBetween\",\"alignItems\":\"center\",\"flexShrink\":0},[\"steps_col\",\"calories_col\"]]\n[\"steps_col\",\"Column\",{\"width\":58,\"justifyContent\":\"center\",\"alignItems\":\"center\",\"itemMargin\":2,\"flexShrink\":0},[\"steps_value\",\"steps_label\"]]\n[\"steps_value\",\"Text\",{\"content\":\"{{ ${/data/health/dailySteps} + '步' }}\",\"fontSize\":18,\"fontWeight\":700,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1}]\n[\"steps_label\",\"Text\",{\"content\":\"步数\",\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#CCFFFFFF\",\"maxLines\":1}]\n[\"calories_col\",\"Column\",{\"width\":58,\"justifyContent\":\"center\",\"alignItems\":\"center\",\"itemMargin\":2,\"flexShrink\":0},[\"calories_value\",\"calories_label\"]]\n[\"calories_value\",\"Text\",{\"content\":{\"path\":\"/data/health/dailyTotalCaloriesText\"},\"fontSize\":18,\"fontWeight\":700,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1}]\n[\"calories_label\",\"Text\",{\"content\":\"热量\",\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#CCFFFFFF\",\"maxLines\":1}]\n[\"sleep_info\",\"Row\",{\"width\":126,\"justifyContent\":\"start\",\"alignItems\":\"center\",\"itemMargin\":6,\"flexShrink\":0},[\"sleep_dot\",\"sleep_text\"]]\n[\"sleep_dot\",\"Image\",{\"src\":\"resources/base/media/moon_z_fill_1.svg\",\"width\":20,\"height\":20,\"objectFit\":\"contain\",\"fillColor\":\"#CCFFFFFF\",\"flexShrink\":0}]\n[\"sleep_text\",\"Text\",{\"content\":\"{{ '睡眠 ' + ${/data/health/sleepScore} + '分 ' + ${/data/health/sleepStatus} }}\",\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1}]\n[\"/data/health/dailySteps\",6200]\n[\"/data/health/dailyTotalCaloriesText\",\"420 千卡\"]\n[\"/data/health/sleepScore\",82]\n[\"/data/health/sleepStatus\",\"良好\"]\n[\"/data/health/nightSleepDurationText\",\"7小时1分\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Stack\",\"children\":[\"fusionBallBackground\",\"__genui_render_component__root\"],\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":0,\"borderRadius\":20,\"clip\":true,\"backgroundColor\":\"#00000000\",\"alignContent\":\"topStart\"}},{\"id\":\"fusionBallBackground\",\"component\":\"Stack\",\"children\":[\"fusionBallLargeSlot\",\"fusionBallMediumSlot\",\"fusionBallSmallSlot\",\"fusionBallGlassLayer\"],\"styles\":{\"width\":\"100%\",\"height\":\"100%\",\"borderRadius\":20,\"alignContent\":\"topStart\",\"clip\":true}},{\"id\":\"fusionBallLargeSlot\",\"component\":\"Stack\",\"children\":[\"fusionBallLarge\"],\"styles\":{\"width\":\"112.5%\",\"height\":\"27.5%\",\"alignContent\":\"center\"}},{\"id\":\"fusionBallLarge\",\"component\":\"Divider\",\"styles\":{\"width\":\"116.666667%\",\"height\":\"477.272727%\",\"strokeWidth\":0,\"color\":\"#00000000\",\"borderRadius\":105,\"backgroundColor\":\"#FFF24131\",\"clip\":true}},{\"id\":\"fusionBallMediumSlot\",\"component\":\"Stack\",\"children\":[\"fusionBallMedium\"],\"styles\":{\"width\":\"50%\",\"height\":\"137.5%\",\"alignContent\":\"bottom\"}},{\"id\":\"fusionBallMedium\",\"component\":\"Divider\",\"styles\":{\"width\":\"200%\",\"height\":\"72.727273%\",\"strokeWidth\":0,\"color\":\"#00000000\",\"borderRadius\":80,\"backgroundColor\":\"#FFFF8833\",\"clip\":true}},{\"id\":\"fusionBallSmallSlot\",\"component\":\"Stack\",\"children\":[\"fusionBallSmall\"],\"styles\":{\"width\":\"121.875%\",\"height\":\"118.75%\",\"alignContent\":\"bottomEnd\"}},{\"id\":\"fusionBallSmall\",\"component\":\"Divider\",\"styles\":{\"width\":\"51.282051%\",\"height\":\"52.631579%\",\"strokeWidth\":0,\"color\":\"#00000000\",\"borderRadius\":50,\"backgroundColor\":\"#FFE68073\",\"clip\":true}},{\"id\":\"fusionBallGlassLayer\",\"component\":\"Divider\",\"styles\":{\"width\":\"100%\",\"height\":\"100%\",\"strokeWidth\":0,\"color\":\"#00000000\",\"backgroundColor\":\"#0DFFFFFF\",\"backdropBlur\":{\"radius\":210}}},{\"id\":\"__genui_render_component__root\",\"component\":\"Column\",\"children\":[\"title_area\",\"content_area\"],\"itemMargin\":4,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"center\",\"justifyContent\":\"start\"}},{\"id\":\"title_area\",\"component\":\"Row\",\"children\":[\"title_area_title\"],\"itemMargin\":0,\"styles\":{\"width\":126,\"height\":20,\"flexShrink\":0,\"justifyContent\":\"start\",\"alignItems\":\"center\"}},{\"id\":\"title_area_title\",\"component\":\"Text\",\"content\":\"运动健康\",\"styles\":{\"width\":126,\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#FFFFFFFF\",\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":0}},{\"id\":\"content_area\",\"component\":\"Column\",\"children\":[\"metrics_row\",\"sleep_info\"],\"itemMargin\":8,\"styles\":{\"width\":126,\"layoutWeight\":1,\"justifyContent\":\"center\",\"alignItems\":\"start\",\"flexShrink\":1}},{\"id\":\"metrics_row\",\"component\":\"Row\",\"children\":[\"steps_col\",\"calories_col\"],\"styles\":{\"width\":126,\"justifyContent\":\"spaceBetween\",\"alignItems\":\"center\",\"flexShrink\":0}},{\"id\":\"steps_col\",\"component\":\"Column\",\"children\":[\"steps_value\",\"steps_label\"],\"itemMargin\":2,\"styles\":{\"width\":58,\"justifyContent\":\"center\",\"alignItems\":\"center\",\"flexShrink\":0}},{\"id\":\"steps_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/health/dailySteps} + '步' }}\",\"styles\":{\"fontSize\":18,\"fontWeight\":700,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1,\"textOverflow\":\"clip\"}},{\"id\":\"steps_label\",\"component\":\"Text\",\"content\":\"步数\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1,\"textOverflow\":\"clip\"}},{\"id\":\"calories_col\",\"component\":\"Column\",\"children\":[\"calories_value\",\"calories_label\"],\"itemMargin\":2,\"styles\":{\"width\":58,\"justifyContent\":\"center\",\"alignItems\":\"center\",\"flexShrink\":0}},{\"id\":\"calories_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/health/dailyTotalCaloriesText} }}\",\"styles\":{\"fontSize\":18,\"fontWeight\":700,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1,\"textOverflow\":\"clip\"}},{\"id\":\"calories_label\",\"component\":\"Text\",\"content\":\"热量\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1,\"textOverflow\":\"clip\"}},{\"id\":\"sleep_info\",\"component\":\"Row\",\"children\":[\"sleep_dot\",\"sleep_text\"],\"itemMargin\":6,\"styles\":{\"width\":126,\"justifyContent\":\"start\",\"alignItems\":\"center\",\"flexShrink\":0}},{\"id\":\"sleep_dot\",\"component\":\"Image\",\"src\":\"resources/base/media/moon_z_fill_1.svg\",\"styles\":{\"width\":20,\"height\":20,\"objectFit\":\"contain\",\"fillColor\":\"#FFFFFFFF\",\"flexShrink\":0}},{\"id\":\"sleep_text\",\"component\":\"Text\",\"content\":\"{{ '睡眠 ' + ${/data/health/sleepScore} + '分 ' + ${/data/health/sleepStatus} }}\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"fontColor\":\"#FFFFFFFF\",\"maxLines\":1,\"textOverflow\":\"clip\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"health\":{\"dailySteps\":6200,\"dailyTotalCaloriesText\":\"420 千卡\",\"sleepScore\":82,\"sleepStatus\":\"良好\",\"nightSleepDurationText\":\"7小时1分\"}}}}}",
  "validationErrors": []
}
```
