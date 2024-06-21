import requests

headers = {
"authority":"www.backmarket.fr",
"method":"GET",
"path":"/fr-fr/l/iphone-14/18f2215c-75ba-4e66-9ead-4264df35ddb7",
"scheme":"https",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding":"gzip, deflate, br, zstd",
"Accept-Language":"fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
"Cache-Control":"max-age=0",
"Cookie":"csrftoken_p=hqQEMqt9syZl5eCoh94jxiSSFaH0j6Lh; sessionid=pgow28freisip3c0clsecpp7iu27mgx2; _gcl_au=1.1.1904969093.1717619789; braze_consent_updated=true; BM_Advertising=true; BM_Analytics=true; BM_User_Experience=true; _gid=GA1.2.141580026.1717619790; _fbp=fb.1.1717619789968.493356552727372697; _tt_enable_cookie=1; _ttp=ACM3TYIs-WIG3Uj6E4fCMHZREaw; FPID=FPID2.2.uT6tNZlYfezeC2Y1hPvT4lwgfImwuoXF82wt%2Bt9Kmoo%3D.1717619790; FPAU=1.1.1904969093.1717619789; _scid=d15fa87c-c1f9-48a2-c97b-a68cf0a567b1; visitor_id=150ccff5-9185-4e06-8d4a-aac95940e3b9; _gcl_aw=GCL.1717662466.CjwKCAjwmYCzBhA6EiwAxFwfgNeDq5kg-493dgvONlVjY_KmGIZB2cTsgY9s6D0WYCm8K6ggLYx-2RoC6sAQAvD_BwE; _gac_UA-55864326-1=1.1717662467.CjwKCAjwmYCzBhA6EiwAxFwfgNeDq5kg-493dgvONlVjY_KmGIZB2cTsgY9s6D0WYCm8K6ggLYx-2RoC6sAQAvD_BwE; FPGCLAW=GCL.1717761013.CjwKCAjwmYCzBhA6EiwAxFwfgNeDq5kg-493dgvONlVjY_KmGIZB2cTsgY9s6D0WYCm8K6ggLYx-2RoC6sAQAvD_BwE; __spdt=0ca3d38d98d142dcb741c0204e6001af; __cf_bm=KOFJL1stWDGNkL18HQlxGi7SM8tXkPJHuWaM7bSa2fA-1717845481-1.0.1.1-F1iT8.SSUQ6y5pgORdS45RUBNaEm5.LhAYBnuAeRfEZxM8BvJrMVOGQY_kFRXEIeANXyxs1W9y895BfJbVnA_yVCMwQHOF1ahDPq5xR16L0; session_id=b6ad2e1b-ba0e-46dd-bf7b-e7cf5b4d7719; FPLC=fpXtTORHyZ24SmrDoy6u8yyAwIS24JG4nNxQ7y87kx%2FnoE10By01NWNGJHUzxP%2FRagkXip2Dfrfy%2B6Hb14A7lPwEZe78t5RAfDSAZXWhhShwfIgdoIQwi7fMVi01uQ%3D%3D; _cs_mk=0.585103561822871_1717841884267; cf_clearance=EZhEyTzTYA1I2ZOKngO2chpuVoPmK5kEva8ly.G.odM-1717845487-1.0.1.1-lJydtOk2Gs0br4xYM1AVlVeDpxjqWwJmqaA3drc12ve6HfWqoo93ruuFxJmmlP3rugfSUYqgNx.CwwY1yBmsyw; tfpsi=3e498635-6fda-4294-9343-0fb1d12c38c5; ab.storage.deviceId.81ecdd2d-d208-4f9e-9180-57c7d045c5c2=%7B%22g%22%3A%22a4bce618-c702-5f13-ba4a-a3b3ade3f1a1%22%2C%22c%22%3A1717841895774%2C%22l%22%3A1717841895774%7D; _ga_123456789=GS1.1.1717841882.6.1.1717843114.0.0.1557416965; _uetsid=49bd44b0237b11efa09b7ff58235d2f3; _uetvid=49bd75a0237b11efa8a8a9091d3d0c16; _uetmsclkid=_uete85de3e3b8a2139d6e1b858362f6c13a; _ga=GA1.2.429085185.1717619790; _rdt_uuid=1717619789596.9e9df8ff-dc29-4b0c-8faf-d50463127e83; amp_b17214=RzRtvZ_ut-qk84oXZM3ksn...1hvrkrmg4.1hvrmsks5.2b.2b.4m; _ga_W101YGMKND=GS1.1.1717841885.8.1.1717843173.1.0.0; _dd_s=logs=1&id=4c0cede5-0041-46ad-a09f-530a4690ad3d&created=1717841883713&expire=1717844072763"
}

url = "https://www.backmarket.fr/fr-fr/l/iphone-14/18f2215c-75ba-4e66-9ead-4264df35ddb7"
response = requests.get(url, headers=headers)


