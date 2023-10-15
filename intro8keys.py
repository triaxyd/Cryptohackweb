

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1_bytes = bytes.fromhex(KEY1)

KEY1withKEY2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key1withkey2_bytes = bytes.fromhex(KEY1withKEY2)

result = key1_bytes ^ key1withkey2_bytes

print(result)