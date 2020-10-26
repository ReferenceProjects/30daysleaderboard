import requests
import time
from bs4 import BeautifulSoup
import fileinput
import json
import concurrent.futures
biglist=[]


url =['https://google.qwiklabs.com/public_profiles/5a46e7fc-72eb-4835-957d-6ee098a6bc41', 'https://google.qwiklabs.com/public_profiles/1e8d5692-d291-4a74-a6a4-5320b293a6e3', 'https://google.qwiklabs.com/public_profiles/64f423b8-f370-499c-95d5-f24302dca89f', 'https://google.qwiklabs.com/public_profiles/a448e717-7a47-4883-8c62-1cf42cf6e077', 'https://google.qwiklabs.com/public_profiles/552f0f41-6313-4fb5-9f93-622cbf99de6a', 'https://www.qwiklabs.com/public_profiles/cbb879f5-8763-4f52-8a60-66e378b561ab', 'https://www.qwiklabs.com/public_profiles/c4fd2b49-5aeb-49e7-9eda-f23440b63a9b', 'https://www.qwiklabs.com/public_profiles/e279a32e-ad10-47d4-a99a-239c45c6a125', 'https://www.qwiklabs.com/public_profiles/b4ee979c-1104-4d77-be1d-9a543ae34a85', 'https://www.qwiklabs.com/public_profiles/4b72f263-a158-4923-bfc7-a1b8b4775445', 'https://www.qwiklabs.com/public_profiles/b99be92b-7d55-4527-901b-3504fa2e8441', 'https://google.qwiklabs.com/public_profiles/4ec67da0-7745-4b03-9998-4ed58ad5db79', 'https://google.qwiklabs.com/public_profiles/0c2ece06-e3ae-4e34-9e71-95fc62f5d89a', 'https://google.qwiklabs.com/public_profiles/d4c9b692-8f5a-4143-8a65-9c0057f67160', 'https://google.qwiklabs.com/public_profiles/b490c2a9-55a8-4011-8aaf-9c6a3c6e07cf', 'https://google.qwiklabs.com/public_profiles/5938a123-c2aa-4e79-8646-0c235faf1522', 'https://google.qwiklabs.com/public_profiles/beb48750-4da9-4d3a-8a9c-307fec78e7dc', 'https://www.qwiklabs.com/public_profiles/bb5d5c04-155d-4c5d-a8fe-d1816131d9b7', 'https://www.qwiklabs.com/public_profiles/728daa7d-41bc-46d8-b625-fa4e9508f252', 'https://google.qwiklabs.com/public_profiles/29c54ad2-3414-46c1-b9de-e28d010b4949', 'https://google.qwiklabs.com/public_profiles/9277193f-de64-4f44-ba2e-0716444ff658', 'https://google.qwiklabs.com/public_profiles/15f11790-bf73-4916-8cc2-3fa401033f64', 'https://google.qwiklabs.com/public_profiles/6eaa46b3-b625-41d1-a457-3c815eb54ca0', 'https://www.qwiklabs.com/public_profiles/2f195cc9-4eb5-4872-95cf-c41c4edb991c', 'https://google.qwiklabs.com/public_profiles/1113b805-bcde-4d23-a1e5-a952f1f7d083', 'https://www.qwiklabs.com/public_profiles/46c7647e-a93c-436f-83af-885b283e1685', 'https://google.qwiklabs.com/public_profiles/fdb070d0-d188-47cd-b9e2-dafb85d30b12', 'https://google.qwiklabs.com/public_profiles/d149bf6e-6fee-47bc-9792-26a42ebbeae2', 'https://www.qwiklabs.com/public_profiles/82e1fe20-6595-435a-b48b-e1b246cf429d', 'https://google.qwiklabs.com/public_profiles/5b1d0b71-f670-46d8-93e7-533392a4e03b', 'https://www.qwiklabs.com/public_profiles/f375ef92-4b39-43ea-ac18-7ffe5179d42a', 'https://google.qwiklabs.com/public_profiles/0604eb20-28bd-44d5-9ca1-e8340bdd915a', 'https://www.qwiklabs.com/public_profiles/54c19001-cd7a-46a2-b6fb-34826a9f33f6', 'https://google-run.qwiklabs.com/public_profiles/540c72dc-f5c4-4961-80bb-920a5adfeccd', 'https://google.qwiklabs.com/public_profiles/722c0072-7f7f-4f44-8380-7e9562a1fbc5', 'https://www.qwiklabs.com/public_profiles/04784e47-307e-4d06-a28f-bda480515ef8', 'https://google.qwiklabs.com/public_profiles/50c749ce-7643-4393-a9ce-b29b39285b9e', 'https://www.qwiklabs.com/public_profiles/8bf1f4a7-2e72-4513-9709-8a6711941efc', 'https://google.qwiklabs.com/public_profiles/b0886b30-bc3e-4bef-a83e-233f0781897b', 'https://www.qwiklabs.com/public_profiles/e3a442a0-8cb1-4a16-b367-df8cfafb272b', 'https://google.qwiklabs.com/public_profiles/57f79d9b-1d4d-4890-ae19-60e3b6a9f8c0', 'https://google.qwiklabs.com/public_profiles/b466903e-392b-4bb1-935b-cb349bd66cda', 'https://google.qwiklabs.com/public_profiles/63aab28f-42fa-4fc5-95a9-2966708f2538', 'https://google.qwiklabs.com/public_profiles/cf9a4a26-424e-46bf-a79d-940b5a68c4bb', 'https://google.qwiklabs.com/public_profiles/03b6cb7a-8c58-49f5-904a-17838b1d8c42', 'https://google.qwiklabs.com/public_profiles/382ddf95-eaa7-42e9-8af7-03dfe36f7e9d', 'https://www.qwiklabs.com/public_profiles/4d8f0e31-9ce3-47da-ae46-752f77d00d6b', 'https://google.qwiklabs.com/public_profiles/b9fdeff2-83be-4cfb-bacc-b749e409ca36', 'https://google.qwiklabs.com/public_profiles/f3ac4cc1-bcca-4d80-bb76-fb33b0dd88bc', 'https://www.qwiklabs.com/public_profiles/c0ccb7cc-5105-48e4-a1ff-964699766c45', 'https://www.qwiklabs.com/public_profiles/fc7abbcb-d3f6-43a1-b4cc-4b75509165a5', 'https://google.qwiklabs.com/public_profiles/b80fc47b-796e-4789-8aab-6e5e310d342d', 'https://google.qwiklabs.com/public_profiles/6c9ea861-488a-4409-b3f1-2378dbfa20a5', 'https://www.qwiklabs.com/public_profiles/40531859-464d-4d3e-aa65-0dc5979c95ad', 'https://google.qwiklabs.com/public_profiles/2e02c291-4267-401f-ac30-043d3b7bd1cc', 'https://google.qwiklabs.com/public_profiles/f29dfac5-ddaf-4d36-9932-6c9801e13fb5', 'https://www.qwiklabs.com/public_profiles/2037c338-27ce-4ec9-a80b-6e2a0fb8abad', 'https://google.qwiklabs.com/public_profiles/6e8f257a-111b-459f-b757-45f5a08facb4', 'https://google.qwiklabs.com/public_profiles/be3dde56-b672-46e0-b447-e32b40b51e75', 'https://www.qwiklabs.com/public_profiles/b9413bfe-d91b-4893-aa46-0d83951b51c1', 'https://google.qwiklabs.com/public_profiles/f028101f-4716-431a-9ff8-6010cc6eb8e7', 'https://google.qwiklabs.com/public_profiles/6eba1ad5-5220-414c-9c3e-69c4bf26e52a', 'https://www.qwiklabs.com/public_profiles/5ecfc9f9-331d-4a5f-bed9-300ad3f3ea9b', 'https://www.qwiklabs.com/public_profiles/f6352ac5-e662-4179-87ea-da8be75cff3d', 'https://google.qwiklabs.com/public_profiles/40e07842-47f9-41e1-a0b9-95cc23b6b5cd', 'https://google.qwiklabs.com/public_profiles/d8ad8a1e-930b-4728-8a6e-d0721ab93365', 'https://www.qwiklabs.com/public_profiles/994b37f7-9797-45b1-a583-7e5480ba92a8', 'https://google.qwiklabs.com/public_profiles/ea47af31-1609-4333-83f3-0093b1d8c784', 'https://run.qwiklabs.com/public_profiles/95a9131a-0d5f-42a1-b63a-bba79c7d83c5', 'https://www.qwiklabs.com/public_profiles/ba4752ee-dfdc-4d40-b970-a45a6c1b1176', 'https://google.qwiklabs.com/public_profiles/60632037-217d-4106-a5c2-2f12cb1479d7', 'https://google.qwiklabs.com/public_profiles/fd7e92a2-be8e-4674-983c-5a6e6be1bc21', 'https://google.qwiklabs.com/public_profiles/112b36b5-2dbd-4642-9dcb-5177a260b5b9', 'https://www.qwiklabs.com/public_profiles/526f58e4-f868-4a66-91f1-49998d1308b8', 'https://www.qwiklabs.com/public_profiles/2614ce88-aed5-4ae1-b31b-e8aaf3841fc4', 'https://google.qwiklabs.com/public_profiles/389338c8-51b4-401b-8714-518d6f5c7eb5', 'https://google.qwiklabs.com/public_profiles/2bcf34df-b830-48e0-b719-056303319587', 'https://www.qwiklabs.com/public_profiles/0e7eee50-1aeb-49a7-966d-e8f7e7c31b02', 'https://google.qwiklabs.com/public_profiles/5360602d-eaa3-4650-8ce6-50b3ec342fec', 'https://www.qwiklabs.com/public_profiles/9af47862-7775-4707-bf71-9ca51cb6e631', 'https://google.qwiklabs.com/public_profiles/b0ab7ef8-6853-4929-a024-9a54bf233c9f', 'https://google.qwiklabs.com/public_profiles/29ad0a3b-a86b-42cd-aba6-c6bcdb372dd1', 'https://google.qwiklabs.com/public_profiles/ab2fcd6c-b083-44bf-9531-62ba418ea422', 'https://google.qwiklabs.com/public_profiles/af47b322-49e9-418e-bde0-e598c79ad62c', 'https://google.qwiklabs.com/public_profiles/2934b289-b8aa-4451-ad0b-238055e5dad2', 'https://google.qwiklabs.com/public_profiles/cd405f00-1445-41b8-9e9d-57b53bf49efd', 'https://google.qwiklabs.com/public_profiles/a9b9e08d-aa65-42bd-8b4c-7f212efbabc9', 'https://google.qwiklabs.com/public_profiles/ef902971-4429-47c6-9b73-60f10f4ddddf', 'https://www.qwiklabs.com/public_profiles/f1e9fe28-3f42-4540-8818-d5a488c83324', 'https://www.qwiklabs.com/public_profiles/6d413e75-2acd-404f-a7c0-892cf17488e3', 'https://www.qwiklabs.com/public_profiles/04b2efd8-7004-4c1d-b53a-1b58873364fb', 'https://www.qwiklabs.com/public_profiles/a9c1f147-4852-4d73-94c8-3ceaab6d2e8f', 'https://google.qwiklabs.com/public_profiles/5e1edb07-ef06-4692-9ac6-3a8c4c2e22c1', 'https://www.qwiklabs.com/public_profiles/1025d6e2-4a45-4814-bd11-35a427b95f6d', 'https://google-run.qwiklabs.com/public_profiles/f8b372c2-ecd9-4a0e-a125-8eb72d3ac0f5', 'https://google.qwiklabs.com/public_profiles/42be566d-86ce-40a0-8d55-70fa7052433a', 'https://google.qwiklabs.com/public_profiles/59e8d480-353d-4b9d-a729-1bf9256b3031', 'https://google.qwiklabs.com/public_profiles/5409e6ff-d688-4bb4-9456-e86031e7ded2', 'https://google.qwiklabs.com/public_profiles/00f523ec-31db-4c84-b12f-851e878d9542', 'https://www.qwiklabs.com/public_profiles/65782af5-9ba9-456f-a6bf-58f1a8e74156', 'https://www.qwiklabs.com/public_profiles/cdc5ea9c-c5a4-482b-90b8-04f0cb05b77c', 'https://www.qwiklabs.com/public_profiles/f8f4ea28-81ad-4fe0-afbb-82a49be1bb12', 'https://google.qwiklabs.com/public_profiles/0e63dc98-0505-4241-bf8f-16590b1e114b', 'https://www.qwiklabs.com/public_profiles/da816952-d06c-43bc-a8e1-9436664f747f', 'https://google.qwiklabs.com/public_profiles/957df389-5a27-4904-a278-46946ec1ec86', 'https://www.qwiklabs.com/public_profiles/27a362f0-14bf-4082-b1ea-b4177d7ee4e0', 'https://google.qwiklabs.com/public_profiles/da3842be-87b9-44ef-8bc9-67c908c12988', 'https://www.qwiklabs.com/public_profiles/595f01b4-9b55-4e4f-9e01-5c85f152e174', 'https://google.qwiklabs.com/public_profiles/7879490e-1e57-4992-8f31-aa5664b69751', 'https://google.qwiklabs.com/public_profiles/091d54e5-b1d6-4a44-9c7a-50c8735d73e0', 'https://google.qwiklabs.com/public_profiles/01d6e680-e507-49e6-a85a-bb93e5af8637', 'https://www.qwiklabs.com/public_profiles/f8b3fb41-18e2-4987-b2a1-e0fc0cff12d3', 'https://google.qwiklabs.com/public_profiles/42593fbb-2a99-4160-be8b-064589ebb5a5', 'https://google.qwiklabs.com/public_profiles/660566ff-85b9-4651-9157-6a9105c512f7', 'https://google.qwiklabs.com/public_profiles/4f0c9805-42be-42d6-a982-b8169d1b9b37', 'https://google.qwiklabs.com/public_profiles/46f0e765-dcc0-4979-a8b4-86aaf4a02a31', 'https://google-run.qwiklabs.com/public_profiles/8c86d118-6c22-4ae7-acd2-35b804d6be50', 'https://google.qwiklabs.com/public_profiles/88418168-2da2-4668-aee8-10fa3665a176', 'https://www.qwiklabs.com/public_profiles/a46722a9-1ac1-488f-811e-57bdb55d664b', 'https://www.qwiklabs.com/public_profiles/ff8a5a2f-00f7-4039-b678-a0fd376d5f85', 'https://google.qwiklabs.com/public_profiles/cae29202-6d34-43a6-be73-2ec93783fe73', 'https://google.qwiklabs.com/public_profiles/ad5c6f77-2e91-4351-baea-10ab4db1a7e0', 'https://google.qwiklabs.com/public_profiles/a9108b75-156b-4890-bc63-5e14385a07e6', 'https://www.qwiklabs.com/public_profiles/9c5db0bd-37e8-4e65-ab9e-1b2b945c7450', 'https://google.qwiklabs.com/public_profiles/82405f41-1646-48d6-9f83-ed959871b14c', 'https://google.qwiklabs.com/public_profiles/120a137f-4e54-40f3-9461-5927721a2cfd', 'https://google.qwiklabs.com/public_profiles/ffa94c93-4a4d-47ec-a598-e72f3d4cb2d1', 'https://www.qwiklabs.com/public_profiles/5597e509-a3d1-4fa8-a3f5-e5d164805fc3', 'https://google.qwiklabs.com/public_profiles/d1daaa52-0f77-494f-9bfe-9da8351752e9', 'https://google.qwiklabs.com/public_profiles/204abbc3-d531-4989-b20f-e4059882127a', 'https://googlecoursera.qwiklabs.com/public_profiles/1636a98b-036c-4b8a-946e-093f88fa987f', 'https://www.qwiklabs.com/public_profiles/48251215-4efe-423a-b392-db92bb867b91', 'https://www.qwiklabs.com/public_profiles/32aebbe5-f9dc-46b5-b6ca-09976cca4a48', 'https://google.qwiklabs.com/public_profiles/6bf0105f-36af-48af-9876-901ad4f89be2', 'https://www.qwiklabs.com/public_profiles/f10c6ccb-dabc-4006-83f3-21d0cd6a2b99', 'https://google.qwiklabs.com/public_profiles/18c014b0-7dd6-4f90-ab2b-b9611faa1b6d', 'https://www.qwiklabs.com/public_profiles/e934087d-996d-4603-a4c7-e7678ccdc7c0', 'https://google.qwiklabs.com/public_profiles/c488c852-1549-4680-9200-2c481c180e50', 'https://www.qwiklabs.com/public_profiles/df3d5e42-31bf-4303-ab38-22db69c21bb1', 'https://google.qwiklabs.com/public_profiles/a7fc487a-cdc5-421e-aa57-1704acd58850', 'https://www.qwiklabs.com/public_profiles/4096abb3-2a1d-4bcd-b370-f37ff376a8c4', 'https://google.qwiklabs.com/public_profiles/6fabc98a-25b3-4144-b611-2b95a33aefda', 'https://google.qwiklabs.com/public_profiles/c613e29c-6c73-4b64-9efb-2bc864fe28bd', 'https://google.qwiklabs.com/public_profiles/e45e8f87-851b-462f-9fb2-3f13c1b7f179', 'https://google.qwiklabs.com/public_profiles/d77a8967-6a74-4b0f-ba0f-09f1e3791d7a', 'https://google.qwiklabs.com/public_profiles/78c397f4-2951-4120-b0f9-4cedc4868c30', 'https://www.qwiklabs.com/public_profiles/67b40ecc-f07e-44e3-9ea4-d22ff49ed23a', 'https://google.qwiklabs.com/public_profiles/800c463d-e44b-446e-be81-a7a1360db551', 'https://www.qwiklabs.com/public_profiles/b04f3dff-400c-4b0a-a0bc-78af1b21c819', 'https://google.qwiklabs.com/public_profiles/7518a7cf-198d-4a2c-8ecf-f093602a5253', 'https://www.qwiklabs.com/public_profiles/b6cd3cc5-a459-45d5-a217-97bfbfa7dc1b', 'https://www.qwiklabs.com/public_profiles/f5a808cb-78e2-476a-8c64-10d7764802d2', 'https://google.qwiklabs.com/public_profiles/b121b1cb-20ed-4894-a806-f0f1fd659a20', 'https://google.qwiklabs.com/public_profiles/20dcd0e8-6216-484c-98c0-ca1b2fd1e26b', 'https://google.qwiklabs.com/public_profiles/9a1c7091-6968-43e8-b84a-86e05e19110b', 'https://google.qwiklabs.com/public_profiles/474c436b-1cf8-4440-a392-d4891f791a69', 'https://google.qwiklabs.com/public_profiles/c18e140e-8f01-44ca-ad36-a7ef76275384', 'https://google.qwiklabs.com/public_profiles/73a46598-fc11-4f78-8cd3-702d76c5b79a', 'https://www.qwiklabs.com/public_profiles/eed1c82d-0b9d-4f0c-b015-fb52367c854c', 'https://google.qwiklabs.com/public_profiles/ae174dd0-4718-47e9-86d0-c4f53b41dfa6', 'https://google.qwiklabs.com/public_profiles/7377b64b-1855-494e-b9a7-97206c09ef08', 'https://google.qwiklabs.com/public_profiles/30d64d7c-b9cd-48ec-9f7c-6a7a4ba95aee', 'https://google.qwiklabs.com/public_profiles/a6139be1-42ad-4241-9749-dbe9e68abd8a', 'https://google.qwiklabs.com/public_profiles/5c7fdd20-e944-4140-87c1-a678cc385791', 'https://google-run.qwiklabs.com/public_profiles/102db44b-eae1-4c37-badb-f27a5e40f311', 'https://www.qwiklabs.com/public_profiles/9b48ecd9-c08d-4ffe-aaf5-0a1a7437a6c9', 'https://www.qwiklabs.com/public_profiles/ca7c13d1-5159-43d5-af0d-2c86662b822c', 'https://www.qwiklabs.com/public_profiles/8714ff56-9806-4061-8a5e-d3f72592a2d1', 'https://www.qwiklabs.com/public_profiles/6c41365b-b27f-4f88-a39f-bbd6ad058f13', 'https://google.qwiklabs.com/public_profiles/7b559a91-1582-4d6c-9932-280d7c130abd', 'https://google.qwiklabs.com/public_profiles/5e09bcbb-24b6-4441-a495-0cc5b38c3421', 'https://google.qwiklabs.com/public_profiles/eb648b74-4327-4c3d-9d11-464377b15663', 'https://www.qwiklabs.com/public_profiles/1f0c95a4-0f9b-4f5b-a319-fd4d1e2582d1', 'https://www.qwiklabs.com/public_profiles/aa6acafc-8970-4b1d-9990-48dc8a12b61e', 'https://google.qwiklabs.com/public_profiles/99e457dd-e105-46de-b696-22b7c4ce31f4', 'https://www.qwiklabs.com/public_profiles/c8b8ee7b-0f1f-48d9-8f24-84f6c1b42ff3', 'https://google.qwiklabs.com/public_profiles/35c6bcb0-b9af-4f49-bcc7-e3874ac2fb74', 'https://qwiklabs.com/public_profiles/d80ef6e7-f9e6-4898-a960-f1926b490e1a', 'https://www.qwiklabs.com/public_profiles/5d8dc359-f803-43e2-8d4e-2d79d933d382', 'https://google.qwiklabs.com/public_profiles/bf6fda0b-f62f-48e2-8129-b9dce94bdc91', 'https://google.qwiklabs.com/public_profiles/96651d8f-78a4-4e7c-bbe1-ce7551177c59', 'https://google.qwiklabs.com/public_profiles/ca587f14-e556-4d68-b699-505ac6e5175b', 'https://google.qwiklabs.com/public_profiles/5c07542d-678d-43d9-908f-85d6e47bd4f0', 'https://google.qwiklabs.com/public_profiles/80b8c161-03c7-479b-8cfc-c65fed11360a', 'https://google-run.qwiklabs.com/public_profiles/b74b5705-8245-4fd4-ab0c-9db44416ee1e', 'https://google.qwiklabs.com/public_profiles/9c4efcb2-d1ee-42ca-b2eb-1e8d0d637cdd', 'https://www.qwiklabs.com/public_profiles/8429cd40-1403-4fc0-820b-34d100325756', 'https://www.qwiklabs.com/public_profiles/6c806fcc-6fe7-4829-99ee-696435603a20', 'https://google.qwiklabs.com/public_profiles/323ee51a-ce4d-4b64-8829-5644959f1dc4', 'https://google.qwiklabs.com/public_profiles/2cf4ee77-0fb9-488d-948c-4da4d6c4b5e5', 'https://google.qwiklabs.com/public_profiles/51f4d25d-2c99-443c-879f-b58480c581c5', 'https://www.qwiklabs.com/public_profiles/06ab771a-e956-4b54-ab42-f6d252ebe3c4', 'https://www.qwiklabs.com/public_profiles/bf5972c4-d4b8-4d5e-a703-27184d2043ee']






track1=[
    'Getting Started: Create and Manage Cloud Resources',
    'Perform Foundational Infrastructure Tasks in Google Cloud',
    'Set up and Configure a Cloud Environment in Google Cloud',
    'Deploy and Manage Cloud Environments with Google Cloud',
    'Build and Secure Networks in Google Cloud',
    'Deploy to Kubernetes in Google Cloud'
    ]
track2 = [
    'Getting Started: Create and Manage Cloud Resources',
    'Perform Foundational Data, ML, and AI Tasks in Google Cloud',
    'Insights from Data with BigQuery',
    'Engineer Data in Google Cloud',
    'Integrate with Machine Learning APIs',
    'Explore Machine Learning Models with Explainable AI'
    ]

def data_scraping (url):
    start_thread(url)

def data_gathering(link):
    tempdic = {}
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    track1completed = []
    track2completed = []
    profile = soup.findAll('div', attrs = {'class':'public-profile__hero'})[0]
    dp = profile.img['src']
    name = profile.h1.text
    tempdic['name'] = name.strip()
    tempdic['dp'] = dp
    quests = soup.findAll('ql-badge')
    for quest in quests:
        allquest = json.loads(quest.get('badge'))['title']
        if allquest in track1:
            track1completed.append(allquest)
        if allquest in track2:
            track2completed.append(allquest)
    tempdic['track1'] = track1completed
    tempdic['track2'] = track2completed
    tempdic['lentrack1'] = len(track1completed)
    tempdic['lentrack2'] = len(track2completed)
    #if tempdic['lentrack1'] == 6 or tempdic['lentrack2'] == 6:
    #    id+=1
    #    print(id,)
    tempdic['qcomplete_no'] = len(track1completed) + len(track2completed)
    if tempdic['qcomplete_no']!=0:
        print(tempdic['name']," got ",tempdic['qcomplete_no']," skill badges")
        biglist.append(tempdic)
        #print("data saved")
    else:
        #print("no badges")
        pass

def data_saving (biglist):
    #num = 0
    res = sorted(biglist, key = lambda x: x['qcomplete_no'], reverse=True)
    print("number of people started",len(res))
    with open("my.json","w") as f:
        json.dump(res,f)
    f.close()
    tk1 = 0
    tk2 = 0
    for tempdic in res:
        x = int(tempdic['lentrack1'])
        y = int(tempdic['lentrack2'])
        if x == 6:
            tk1+=1
        if y == 6:
            tk2+=1
    print("Number of people completed track 1 : ",tk1)
    print("Number of people completed track 2 : ",tk2)
    print("Number of people completed atleast 1 track : ",tk1+tk2)
    #print("number of people completed atleast one track ",num)
    #print(res)


def start_thread(url2):
    threads = 15
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(data_gathering, url2)
    data_saving (biglist)

def main(url):
    data_scraping (url)

if __name__ == '__main__':
    t0 = time.time()
    id = 0
    main(url)
    t1 = time.time()
    print(f"{t1-t0} seconds to download {len(url)} profile.")
    #print("number of people completed atleast one track",id)
