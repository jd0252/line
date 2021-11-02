{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "ConnectionError",
     "evalue": "HTTPConnectionPool(host='www.twse.com.tw', port=80): Max retries exceeded with url: /exchangeReport/STOCK_DAY?date=20210801&stockNo=2330 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x00000228C7545E50>: Failed to establish a new connection: [WinError 10060] 連線嘗試失敗，因為連線對象有一段時間並未正確回應，或是連線建立失敗，因為連線的主機無法回應。'))",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTimeoutError\u001b[0m                              Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36m_new_conn\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    168\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 169\u001b[1;33m             conn = connection.create_connection(\n\u001b[0m\u001b[0;32m    170\u001b[0m                 \u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_dns_host\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mport\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mextra_kw\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\urllib3\\util\\connection.py\u001b[0m in \u001b[0;36mcreate_connection\u001b[1;34m(address, timeout, source_address, socket_options)\u001b[0m\n\u001b[0;32m     95\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0merr\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 96\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     97\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\urllib3\\util\\connection.py\u001b[0m in \u001b[0;36mcreate_connection\u001b[1;34m(address, timeout, source_address, socket_options)\u001b[0m\n\u001b[0;32m     85\u001b[0m                 \u001b[0msock\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msource_address\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 86\u001b[1;33m             \u001b[0msock\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msa\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     87\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0msock\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTimeoutError\u001b[0m: [WinError 10060] 連線嘗試失敗，因為連線對象有一段時間並未正確回應，或是連線建立失敗，因為連線的主機無法回應。",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mNewConnectionError\u001b[0m                        Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    698\u001b[0m             \u001b[1;31m# Make the request on the httplib connection object.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 699\u001b[1;33m             httplib_response = self._make_request(\n\u001b[0m\u001b[0;32m    700\u001b[0m                 \u001b[0mconn\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36m_make_request\u001b[1;34m(self, conn, method, url, timeout, chunked, **httplib_request_kw)\u001b[0m\n\u001b[0;32m    393\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 394\u001b[1;33m                 \u001b[0mconn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mhttplib_request_kw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    395\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(self, method, url, body, headers)\u001b[0m\n\u001b[0;32m    233\u001b[0m             \u001b[0mheaders\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"User-Agent\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_get_default_user_agent\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 234\u001b[1;33m         \u001b[0msuper\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mHTTPConnection\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    235\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\http\\client.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[0;32m   1254\u001b[0m         \u001b[1;34m\"\"\"Send a complete request to the server.\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1255\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_send_request\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1256\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\http\\client.py\u001b[0m in \u001b[0;36m_send_request\u001b[1;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[0;32m   1300\u001b[0m             \u001b[0mbody\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_encode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'body'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1301\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mendheaders\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mencode_chunked\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1302\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\http\\client.py\u001b[0m in \u001b[0;36mendheaders\u001b[1;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[0;32m   1249\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mCannotSendHeader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1250\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_send_output\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage_body\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mencode_chunked\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1251\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\http\\client.py\u001b[0m in \u001b[0;36m_send_output\u001b[1;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[0;32m   1009\u001b[0m         \u001b[1;32mdel\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_buffer\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1010\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1011\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\http\\client.py\u001b[0m in \u001b[0;36msend\u001b[1;34m(self, data)\u001b[0m\n\u001b[0;32m    949\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mauto_open\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 950\u001b[1;33m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    951\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36mconnect\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    199\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 200\u001b[1;33m         \u001b[0mconn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_new_conn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    201\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_prepare_conn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mconn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36m_new_conn\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    180\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mSocketError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 181\u001b[1;33m             raise NewConnectionError(\n\u001b[0m\u001b[0;32m    182\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"Failed to establish a new connection: %s\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNewConnectionError\u001b[0m: <urllib3.connection.HTTPConnection object at 0x00000228C7545E50>: Failed to establish a new connection: [WinError 10060] 連線嘗試失敗，因為連線對象有一段時間並未正確回應，或是連線建立失敗，因為連線的主機無法回應。",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mMaxRetryError\u001b[0m                             Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\requests\\adapters.py\u001b[0m in \u001b[0;36msend\u001b[1;34m(self, request, stream, timeout, verify, cert, proxies)\u001b[0m\n\u001b[0;32m    438\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mchunked\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 439\u001b[1;33m                 resp = conn.urlopen(\n\u001b[0m\u001b[0;32m    440\u001b[0m                     \u001b[0mmethod\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    754\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 755\u001b[1;33m             retries = retries.increment(\n\u001b[0m\u001b[0;32m    756\u001b[0m                 \u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merror\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0m_pool\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0m_stacktrace\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexc_info\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\urllib3\\util\\retry.py\u001b[0m in \u001b[0;36mincrement\u001b[1;34m(self, method, url, response, error, _pool, _stacktrace)\u001b[0m\n\u001b[0;32m    573\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mnew_retry\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mis_exhausted\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 574\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mMaxRetryError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m_pool\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merror\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0mResponseError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcause\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    575\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mMaxRetryError\u001b[0m: HTTPConnectionPool(host='www.twse.com.tw', port=80): Max retries exceeded with url: /exchangeReport/STOCK_DAY?date=20210801&stockNo=2330 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x00000228C7545E50>: Failed to establish a new connection: [WinError 10060] 連線嘗試失敗，因為連線對象有一段時間並未正確回應，或是連線建立失敗，因為連線的主機無法回應。'))",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mConnectionError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-10-c8ab96995706>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mtwstock\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mStock\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mtw2330\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mStock\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"2330\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mtype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtw2330\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mtw2330\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprice\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\twstock\\stock.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, sid, initial_fetch)\u001b[0m\n\u001b[0;32m    152\u001b[0m         \u001b[1;31m# Init data\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    153\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0minitial_fetch\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 154\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfetch_31\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    155\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    156\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_month_year_iter\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstart_month\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstart_year\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend_month\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend_year\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\twstock\\stock.py\u001b[0m in \u001b[0;36mfetch_31\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    181\u001b[0m         \u001b[0mtoday\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdatetime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtoday\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    182\u001b[0m         \u001b[0mbefore\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtoday\u001b[0m \u001b[1;33m-\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtimedelta\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdays\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m60\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 183\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfetch_from\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbefore\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0myear\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbefore\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmonth\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    184\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m31\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    185\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\twstock\\stock.py\u001b[0m in \u001b[0;36mfetch_from\u001b[1;34m(self, year, month)\u001b[0m\n\u001b[0;32m    173\u001b[0m         \u001b[0mtoday\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdatetime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtoday\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    174\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0myear\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmonth\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_month_year_iter\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmonth\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0myear\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtoday\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmonth\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtoday\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0myear\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 175\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mraw_data\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfetcher\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfetch\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0myear\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmonth\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msid\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    176\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mextend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mraw_data\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'data'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    177\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\twstock\\stock.py\u001b[0m in \u001b[0;36mfetch\u001b[1;34m(self, year, month, sid, retry)\u001b[0m\n\u001b[0;32m     56\u001b[0m         \u001b[0mparams\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;34m'date'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m'%d%02d01'\u001b[0m \u001b[1;33m%\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0myear\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmonth\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'stockNo'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0msid\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     57\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mretry_i\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mretry\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 58\u001b[1;33m             r = requests.get(self.REPORT_URL, params=params,\n\u001b[0m\u001b[0;32m     59\u001b[0m                              proxies=get_proxies())\n\u001b[0;32m     60\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\requests\\api.py\u001b[0m in \u001b[0;36mget\u001b[1;34m(url, params, **kwargs)\u001b[0m\n\u001b[0;32m     74\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     75\u001b[0m     \u001b[0mkwargs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msetdefault\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'allow_redirects'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 76\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'get'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mparams\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     77\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     78\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\requests\\api.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(method, url, **kwargs)\u001b[0m\n\u001b[0;32m     59\u001b[0m     \u001b[1;31m# cases, and look like a memory leak in others.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     60\u001b[0m     \u001b[1;32mwith\u001b[0m \u001b[0msessions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSession\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0msession\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 61\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0msession\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     62\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     63\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\requests\\sessions.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)\u001b[0m\n\u001b[0;32m    540\u001b[0m         }\n\u001b[0;32m    541\u001b[0m         \u001b[0msend_kwargs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msettings\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 542\u001b[1;33m         \u001b[0mresp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mprep\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0msend_kwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    543\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    544\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mresp\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\requests\\sessions.py\u001b[0m in \u001b[0;36msend\u001b[1;34m(self, request, **kwargs)\u001b[0m\n\u001b[0;32m    653\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    654\u001b[0m         \u001b[1;31m# Send the request\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 655\u001b[1;33m         \u001b[0mr\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0madapter\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    656\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    657\u001b[0m         \u001b[1;31m# Total elapsed time of the request (approximately)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\requests\\adapters.py\u001b[0m in \u001b[0;36msend\u001b[1;34m(self, request, stream, timeout, verify, cert, proxies)\u001b[0m\n\u001b[0;32m    514\u001b[0m                 \u001b[1;32mraise\u001b[0m \u001b[0mSSLError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    515\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 516\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mConnectionError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    517\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    518\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mClosedPoolError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mConnectionError\u001b[0m: HTTPConnectionPool(host='www.twse.com.tw', port=80): Max retries exceeded with url: /exchangeReport/STOCK_DAY?date=20210801&stockNo=2330 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x00000228C7545E50>: Failed to establish a new connection: [WinError 10060] 連線嘗試失敗，因為連線對象有一段時間並未正確回應，或是連線建立失敗，因為連線的主機無法回應。'))"
     ]
    }
   ],
   "source": [
    "\n",
    "from twstock import Stock \n",
    "tw2330=Stock(\"2330\") \n",
    "type(tw2330) \n",
    "tw2330.price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import twstock\n",
    "import pandas_datareader as web\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 下載醉心收盤價價\n",
    "close = web.DataReader(name='^TWII', data_source='yahoo',start='2021-01-01')['Close'][-1]\n",
    "original=16408.35\n",
    "market_ret=(close-original)/original"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "stocklist=['2317',\n",
    "'6415',\n",
    "'6488',\n",
    "'2881',\n",
    "'2882',\n",
    "'2454',\n",
    "'2886',\n",
    "'6282',\n",
    "'3141',\n",
    "'5483',\n",
    "'2727',\n",
    "'8255',\n",
    "'2634',\n",
    "'8069',\n",
    "'8454']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "cost=['103.75',\n",
    "'3935',\n",
    "'758',\n",
    "'74.95',\n",
    "'56.8',\n",
    "'869',\n",
    "'33',\n",
    "'28.8',\n",
    "'139',\n",
    "'174.5',\n",
    "'157.5',\n",
    "'194.75',\n",
    "'28.35',\n",
    "'71.5',\n",
    "'1575']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=twstock.realtime.get(stocklist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "e = datetime.datetime.today()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "ret=0\n",
    "message=f'現在時間 {e:%Y-%m-%d (%a) %H:%M:%S}\\n'\n",
    "for i,j in zip(stocklist,range(len(stocklist))):\n",
    "    n=df[i]['info']['name']\n",
    "    p=float(df[i]['realtime']['best_bid_price'][1])\n",
    "    c=float(cost[j])\n",
    "    r=round((p-c)/c*100,2)\n",
    "    ret+=r\n",
    "    message+=f'{j+1} {n:.5s} 現價 {p:.0f} 成本 {c:.0f} 報酬率 {r}% \\n'\n",
    "message+=f'\\n-----------總結----------- \\n當日大盤{close:.2f}\\n 10/4大盤 {original:.2f} \\n 大盤報酬 {market_ret*100:.2f} % 投組報酬 {ret/15:.2f} →{ret/15-market_ret*100:.2f} %  \\n'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "3phkQGXne9Uv"
   },
   "source": [
    "----\n",
    "## Line API\n",
    "\n",
    "- - 申請開發者帳號\n",
    "- 申請line token\n",
    "- 以自己的token進行自己的警報"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "nXZvkMsUe9Uv"
   },
   "source": [
    "- 第一個LINE通知服務練習: 請修改\"Title\"中的文字，以便分辨是自己傳送成功"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "UhiXSSSLe9Uw"
   },
   "outputs": [],
   "source": [
    "# 課程的token\n",
    "# 由：https://notify-bot.line.me/my/ 取得\n",
    "#0x9AUj9ueQDuJGXEO62djREkZO5AJ7BofSlRyYQByBz\n",
    "#BtBGtRC9DhF9riBGPfD5ODTl5J3C4A8dFPOMCEQzDcm\n",
    "token = '0x9AUj9ueQDuJGXEO62djREkZO5AJ7BofSlRyYQByBz'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "dyERf-6se9Uw",
    "outputId": "9407a2f8-959a-40b6-8827-8e8d13f6f817"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Response [200]>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "url = \"https://notify-api.line.me/api/notify\"  # --> 不支援http, 只能用https\n",
    "headers = {\"Authorization\" : \"Bearer \"+ token}\n",
    "#message=\"123 '%0D%0A' 456\"\n",
    "title = '測試'\n",
    "payload = {\"message\" :  message}\n",
    "\n",
    "r = requests.post(url ,headers = headers ,params=payload)\n",
    "r"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [],
   "name": "linesample",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
