import requests
import json
import time
from datetime import datetime

cookies = {
    'HSID': 'A1guUq2MCvuKfAdVo',
    'SSID': 'AF5E45R7zZ1gcNPbp',
    'APISID': '479ooRGen5K9XIOo/ABsPRLe8OUU-DGdUd',
    'SAPISID': 'O2Bi1r7wopyQNlLM/A6He0V4KPzpcmpvN_',
    '__Secure-1PAPISID': 'O2Bi1r7wopyQNlLM/A6He0V4KPzpcmpvN_',
    '__Secure-3PAPISID': 'O2Bi1r7wopyQNlLM/A6He0V4KPzpcmpvN_',
    'S': 'billing-ui-v3=EyNFAtUcR47wpu30aeKZaKUQaba31JLG:billing-ui-v3-efe=EyNFAtUcR47wpu30aeKZaKUQaba31JLG',
    'SEARCH_SAMESITE': 'CgQI5ZgB',
    'SID': 'ZwjEYlwJldFXnIXYG1vG4sNHF9z4J2uY5xO0dD9ZMm_21U2MQhwgap7oSLk6shdof9j8bg.',
    '__Secure-1PSID': 'ZwjEYlwJldFXnIXYG1vG4sNHF9z4J2uY5xO0dD9ZMm_21U2Mj_06uE3JzQjFu9eX96MKTw.',
    '__Secure-3PSID': 'ZwjEYlwJldFXnIXYG1vG4sNHF9z4J2uY5xO0dD9ZMm_21U2MnzD_tBbzoDRxLKg2GoNYkQ.',
    'AEC': 'Ad49MVGJSeaaBXU_JiDj72Ak3QqZ0BP1_BVXb78Xjp_b0Eo8Z1Z4YP0BzLc',
    'NID': '511=lduMqpskNbnPiLIaH7rgHJY83Ehf0Eqp1i3tfrUArlyIH2ub5i9StgYcaHuZvDeXnj4TvMlv0lMKkoj-BgVso3vF3V0OU4_y-txjuWs5VcXHD1D_Ta317QIiM2304Ha3hcjhSBTfP2mQ3l7HYSj-ZtTJGEOkCF71u0WjRhAT-epLR9MaHC1Vri99RJLFjGagfMnIW1e5XfI_2_lqwxpnnUwM-1BbMqt4TW0_LLd6METW4o21RmuN5fmBnG6O4FQBv0koo11xZJf6VODIjKbggxcpE6nQO9nGn78',
    'OTZ': '7191246_80_84_104220_80_446880',
    '1P_JAR': '2023-9-3-22',
    '__Secure-1PSIDTS': 'sidts-CjEBSAxbGRXcBTdh2oAJJPF9ZVSP-uvWsA3NSXPygh2sCXnTRaXWXjuXc2I8eJ7VIHqlEAA',
    '__Secure-3PSIDTS': 'sidts-CjEBSAxbGRXcBTdh2oAJJPF9ZVSP-uvWsA3NSXPygh2sCXnTRaXWXjuXc2I8eJ7VIHqlEAA',
    'SIDCC': 'APoG2W8_arwxY9CpIkNu_Ci13EJSPMLmMgAnrFrPJuqdVpx53A7CHIaj6X-Ogiaw3v5S-P3aNB8',
    '__Secure-1PSIDCC': 'APoG2W_ZkgTIhljxvw3Ea0JL5j2EWkOzBmlRAERet5KOU1jVwZRZ2RX7tqOGypsg62susE1ONVo',
    '__Secure-3PSIDCC': 'APoG2W8dV9mOX2i9uSoMc2o9FkXCe3rUO8sj3UxRdJpNlBKB_ZPm1UcEe3iJi5iq4li6QHKPLRo1',
}

headers = {
    'authority': 'trends.google.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'HSID=A1guUq2MCvuKfAdVo; SSID=AF5E45R7zZ1gcNPbp; APISID=479ooRGen5K9XIOo/ABsPRLe8OUU-DGdUd; SAPISID=O2Bi1r7wopyQNlLM/A6He0V4KPzpcmpvN_; __Secure-1PAPISID=O2Bi1r7wopyQNlLM/A6He0V4KPzpcmpvN_; __Secure-3PAPISID=O2Bi1r7wopyQNlLM/A6He0V4KPzpcmpvN_; S=billing-ui-v3=EyNFAtUcR47wpu30aeKZaKUQaba31JLG:billing-ui-v3-efe=EyNFAtUcR47wpu30aeKZaKUQaba31JLG; SEARCH_SAMESITE=CgQI5ZgB; SID=ZwjEYlwJldFXnIXYG1vG4sNHF9z4J2uY5xO0dD9ZMm_21U2MQhwgap7oSLk6shdof9j8bg.; __Secure-1PSID=ZwjEYlwJldFXnIXYG1vG4sNHF9z4J2uY5xO0dD9ZMm_21U2Mj_06uE3JzQjFu9eX96MKTw.; __Secure-3PSID=ZwjEYlwJldFXnIXYG1vG4sNHF9z4J2uY5xO0dD9ZMm_21U2MnzD_tBbzoDRxLKg2GoNYkQ.; AEC=Ad49MVGJSeaaBXU_JiDj72Ak3QqZ0BP1_BVXb78Xjp_b0Eo8Z1Z4YP0BzLc; NID=511=lduMqpskNbnPiLIaH7rgHJY83Ehf0Eqp1i3tfrUArlyIH2ub5i9StgYcaHuZvDeXnj4TvMlv0lMKkoj-BgVso3vF3V0OU4_y-txjuWs5VcXHD1D_Ta317QIiM2304Ha3hcjhSBTfP2mQ3l7HYSj-ZtTJGEOkCF71u0WjRhAT-epLR9MaHC1Vri99RJLFjGagfMnIW1e5XfI_2_lqwxpnnUwM-1BbMqt4TW0_LLd6METW4o21RmuN5fmBnG6O4FQBv0koo11xZJf6VODIjKbggxcpE6nQO9nGn78; OTZ=7191246_80_84_104220_80_446880; 1P_JAR=2023-9-3-22; __Secure-1PSIDTS=sidts-CjEBSAxbGRXcBTdh2oAJJPF9ZVSP-uvWsA3NSXPygh2sCXnTRaXWXjuXc2I8eJ7VIHqlEAA; __Secure-3PSIDTS=sidts-CjEBSAxbGRXcBTdh2oAJJPF9ZVSP-uvWsA3NSXPygh2sCXnTRaXWXjuXc2I8eJ7VIHqlEAA; SIDCC=APoG2W8_arwxY9CpIkNu_Ci13EJSPMLmMgAnrFrPJuqdVpx53A7CHIaj6X-Ogiaw3v5S-P3aNB8; __Secure-1PSIDCC=APoG2W_ZkgTIhljxvw3Ea0JL5j2EWkOzBmlRAERet5KOU1jVwZRZ2RX7tqOGypsg62susE1ONVo; __Secure-3PSIDCC=APoG2W8dV9mOX2i9uSoMc2o9FkXCe3rUO8sj3UxRdJpNlBKB_ZPm1UcEe3iJi5iq4li6QHKPLRo1',
    'referer': 'https://trends.google.com/trends/explore?geo=US&hl=en-US',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"12.6.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://trends.google.com/trends/api/widgetdata/relatedsearches?hl=en-US&tz=360&req=%7B%22restriction%22:%7B%22geo%22:%7B%22country%22:%22US%22%7D,%22time%22:%222022-09-03+2023-09-03%22,%22originalTimeRangeForExploreUrl%22:%22today+12-m%22%7D,%22keywordType%22:%22QUERY%22,%22metric%22:%5B%22TOP%22,%22RISING%22%5D,%22trendinessSettings%22:%7B%22compareTime%22:%222021-09-02+2022-09-02%22%7D,%22requestOptions%22:%7B%22property%22:%22%22,%22backend%22:%22IZG%22,%22category%22:0%7D,%22language%22:%22en%22,%22userCountryCode%22:%22US%22,%22userConfig%22:%7B%22userType%22:%22USER_TYPE_LEGIT_USER%22%7D%7D&token=APP6_UEAAAAAZPZVl1szCPm6Pbm6m6Av9ysLLAov9eKx',
    cookies=cookies,
    headers=headers,
)

file_path = "trends.txt"

while True:

  json_data = response.text

  json_data = (json_data).split('\n', 1)[1]  #Remove the initial characters before the JSON data

  data = json.loads(json_data)

  ranked = data['default']['rankedList'][1]['rankedKeyword']

  trend = [item['query'] for item in ranked]

  current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  row = f"{current_time}, {', '.join(trend)}"

  with open(file_path, 'a') as file:
    
    file.write(str(row) + "\n")

  print(trend)
  
  time.sleep(60)
