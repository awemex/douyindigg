import requests
import json
#替换下面参数
iid='XX'
device_id='XX'
aweme_id = 'XX'
cdid='XXX'
token='XXX'
url = f'https://api26-normal-hl.amemv.com/aweme/v1/commit/item/digg/?ac=WIFI&aid=1128&appTheme=light&app_name=aweme&app_version=24.8.0&build_number=248012&cdid={cdid}&channel=App+Store&device_id={device_id}&device_platform=iphone&device_type=iPhone10%2C3&iid={iid}&is_guest_mode=0&is_vcd=1&js_sdk_version=2.85.0.20&mcc_mnc=&md=0&minor_status=0&need_personal_recommend=1&os_api=18&os_version=13.6&package=com.ss.iphone.ugc.Aweme&screen_width=&tma_jssdk_version=2.85.0.20&version_code=24.8.0'
payload = f'nearby_level=0&friend_recommend=0&type=1&aweme_id={aweme_id}&channel_id=13&is_commerce=0'



gxurl = "https://24dy.com/api/ios/dy_argus"

gxpayload = json.dumps({
  "url": url,
  "method": "post",
  "body": payload,
  #解密原始xa拿到的参数
  "device_id": device_id,
  "gorgon_sdk_version_str": "01010404",
  "appid": "1128",
  "app_version": "24.8.0",
  "argus_sdk_version_str": "v04.04.01-ml-iOS",
  "argus_sdk_version": 134742530,
  "argus_devices_token": ""
  #//end
})
gxheaders = {
  'auth': '9959be5dd8490410f2bb41b2ba92ccec',
  'Content-Type': 'application/json'
}

response = requests.request("POST", gxurl, headers=gxheaders, data=gxpayload)
print(response.text)
#拿到签名
json_response = json.loads(response.text)

headers = {
  'Host': 'api26-normal-hl.amemv.com',
  'User-Agent': 'Aweme 24.8.0 rv:248012 (iPhone; iOS 13.6; en_CN) Cronet',
  'Accept-Encoding': 'gzip, deflate, br',
  'Passport-Sdk-Version': '5.14.1-rc.5-douyin',
  'Sdk-Version': '2',
  'X-Argus': json_response['data']['x_argus'],
  'X-Bd-Kmsv': '1',
  'X-Gorgon': json_response['data']['x_gorgon'],
  'X-Khronos': json_response['data']['x_khronos'],
  'X-Ladon': json_response['data']['x_ladon'],
  'X-Ss-Dp': '1128',
  'X-Ss-Stub': json_response['data']['x_ss_stub'],
  'X-Tt-Request-Tag': 's=-1',
  'X-Tt-Token': token,
  'X-Vc-Bdturing-Sdk-Version': '3.6.1',
  'Content-Type': 'application/x-www-form-urlencoded'
}


response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
