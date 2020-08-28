# locust_sample
Locustを試しに動かしてみる

https://github.com/nnashiki/fastapi_mock_api に向けてAPIを飛ばすサンプル
(localhostに向けると動かないので注意が必要)

```
docker run -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py --host http://localhost:8080
```

## rfs.
- https://docs.locust.io/en/stable/configuration.html#all-available-configuration-options
