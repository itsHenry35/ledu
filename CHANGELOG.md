# Changelog

## 1.0.0 (2025-01-22)


### ⚠ BREAKING CHANGES

* import aria2c from motrix

### Features

* A button to open the downloading folder has been added ([69b6b99](https://github.com/itsHenry35/ledu/commit/69b6b996657fab3890f03f7375171d87a855a73d))
* add error handling and error reporting ([c60795e](https://github.com/itsHenry35/ledu/commit/c60795e772a724cdf9327c10b28e483062c58bef))
* add subject name to the downloaded files ([ea0d690](https://github.com/itsHenry35/ledu/commit/ea0d6901ed38644323bd42d179f7fa45c70c2cb6))
* ask the user whether to open error reporting website ([bf8e9de](https://github.com/itsHenry35/ledu/commit/bf8e9de5c6600951ddf610b110c6f06a99614722))
* avoid path permission denials ([a163f16](https://github.com/itsHenry35/ledu/commit/a163f16466fadea8f4943da692c39fe9debd5eaf))
* better layout ([ff2a50f](https://github.com/itsHenry35/ledu/commit/ff2a50fc8e9923f096072b6e0fe22d97ae5c4a35))
* don't pop up aria2 window ([a7a27e4](https://github.com/itsHenry35/ledu/commit/a7a27e44dc7343809d2e7cf2c9b34996d718c719))
* import aria2c from motrix ([829e7ab](https://github.com/itsHenry35/ledu/commit/829e7ab078dc5d62d8a3fc3bb0a3a69bdc68796e))
* new url place support and support for "无回放"courses ([ad6f275](https://github.com/itsHenry35/ledu/commit/ad6f2750e8e7c1a56ac02f6979fc89aa4862df49))
* pause / resume button ([c5e2467](https://github.com/itsHenry35/ledu/commit/c5e2467a74ad3bdb0bebf60a704f82d931f7aeb8))
* replace illegal characters ([f4eef4c](https://github.com/itsHenry35/ledu/commit/f4eef4c6bbdc57806e827df3dcac672e0c97d8db))
* show progress (eg. 2/4 downloaded) ([7e1ef46](https://github.com/itsHenry35/ledu/commit/7e1ef46b932f38f1201c3f027be7742cd254b294))
* support 'COMBINE_SMALL_CLASS_MODE' ([576336d](https://github.com/itsHenry35/ledu/commit/576336dcf7bd914c5226b20a10a0ee629cc9b21d))
* support dynamic window resizing ([084da8c](https://github.com/itsHenry35/ledu/commit/084da8cf9059666a64ddd7feec3aeb29b6ddcd31))
* support multi course downloading and custom download path ([bd5c3bf](https://github.com/itsHenry35/ledu/commit/bd5c3bff983efbde6577ecda09a009a770e1d1ce))
* support non-override ([12db284](https://github.com/itsHenry35/ledu/commit/12db2844aa23d89d734535e8ce7e34aa079d8f50))
* support scrollbar ([2ca84be](https://github.com/itsHenry35/ledu/commit/2ca84befd7bbaf703a3cb54f9d14a646ebfbb626))


### Bug Fixes

* also fix unexpected response for record_mode [skip ci] ([76a6c79](https://github.com/itsHenry35/ledu/commit/76a6c7918209fe6234ec3010478ae79269bb9955))
* aria2 override params ([3d93f59](https://github.com/itsHenry35/ledu/commit/3d93f5931e340e357e1b8e3ffb0de20f83ea806c))
* Chinese typo [skip ci] ([b1fb9d9](https://github.com/itsHenry35/ledu/commit/b1fb9d941d439dbdef2961d9195c9ef6d9bcdd8e))
* do not commit complied python files ([09fa9bd](https://github.com/itsHenry35/ledu/commit/09fa9bd3366507d1eb104a921a185a383d4c4d89))
* double quote to avoid usernames with a space on Windows ([2473d26](https://github.com/itsHenry35/ledu/commit/2473d26af02ef74d1da1a11a4c892de2834158fe))
* error downloading after switching back from sms ([2083921](https://github.com/itsHenry35/ledu/commit/2083921e4083f79a039b755a646b8ba7444420e6))
* fix logical error when error password occurs ([0b41246](https://github.com/itsHenry35/ledu/commit/0b41246aedafae6c261b7e2518d3a2461230a38c))
* fix the error if the class hasn't started yet ([1f3513a](https://github.com/itsHenry35/ledu/commit/1f3513af1c3fa9c73b3b350556b7a064261cf53f))
* Progress will be 99 percent even if the download has completed ([69b6b99](https://github.com/itsHenry35/ledu/commit/69b6b996657fab3890f03f7375171d87a855a73d))
* sms not defined error while closing ([cf425ea](https://github.com/itsHenry35/ledu/commit/cf425ea43b573b2b2ec1062cdf57c2ea26ddc689))
* sometimes video_data doesn't exist ([08c2b50](https://github.com/itsHenry35/ledu/commit/08c2b50e399655f340639ace3b1933ff927c6705))
* Switching between sms and pwd may trigger loop ([343c9a3](https://github.com/itsHenry35/ledu/commit/343c9a3ddcf059dc5809bba466a714e35cbd00fd))
* syntax error powershell varieble ([a90ad05](https://github.com/itsHenry35/ledu/commit/a90ad0569d2027851bedc5f9b1ea605aeee0d25a))
* unable to download in linux ([3609d3f](https://github.com/itsHenry35/ledu/commit/3609d3f098ab190b2e49ef65f794e38af58003cc))
* undefined var when exiting ([ef66a41](https://github.com/itsHenry35/ledu/commit/ef66a41d98ba0128d2a40ad8843437be164276a4))


### Docs

* improve error feedback ([3816138](https://github.com/itsHenry35/ledu/commit/38161385419a6946624f9de26d97db9a85a600ec))


### Code Refactoring

* add newline at end of file ([c96f753](https://github.com/itsHenry35/ledu/commit/c96f753ccb0155690c4851a7db88df1bee0fa530))
* code refactor with idea [skip CI] ([dbb7edf](https://github.com/itsHenry35/ledu/commit/dbb7edf592b64837eee7e604fd4f3effe9a53332))
* convert string with anomalous backslash into a raw string ([91d67fc](https://github.com/itsHenry35/ledu/commit/91d67fcd660cd8b802aa936a7b6c6b07fd5a0bbe))
* convert string with anomalous backslash into a raw string ([91d67fc](https://github.com/itsHenry35/ledu/commit/91d67fcd660cd8b802aa936a7b6c6b07fd5a0bbe))
* convert string with anomalous backslash into a raw string ([9494c77](https://github.com/itsHenry35/ledu/commit/9494c77331ceb655d6cc06f7339c5dad7301aca5))
* import packages in separate lines ([bc4e160](https://github.com/itsHenry35/ledu/commit/bc4e160b0347986ee61c745a2408143f184abf08))
* refactor `if` expression ([03a749c](https://github.com/itsHenry35/ledu/commit/03a749cd5c99b5c7cbe336be875e1d0da63d8c47))
* refactor for code regulation with pycharm ([97bb384](https://github.com/itsHenry35/ledu/commit/97bb3843f8ef56aa323fcf934716a87829da6344))
* refactor unnecessary `else` / `elif` when `if` block has a `raise` statement ([4c54ea5](https://github.com/itsHenry35/ledu/commit/4c54ea5be7a7639c0fb9d0a6d00b7c83f9c46551))
* refactor unnecessary `else` / `elif` when `if` block has a `raise` statement ([4c54ea5](https://github.com/itsHenry35/ledu/commit/4c54ea5be7a7639c0fb9d0a6d00b7c83f9c46551))
* refactor unnecessary `else` / `elif` when `if` block has a `raise` statement ([e5c15ef](https://github.com/itsHenry35/ledu/commit/e5c15ef3f60855bc3429846439aa5feebb5390e7))
* refactor unnecessary `else` / `elif` when `if` block has a `return` statement ([c44fb19](https://github.com/itsHenry35/ledu/commit/c44fb19ffc488dfbaa96694aeede51b7c8e4124b))
* refactor useless `else` block in the loop ([8dc935c](https://github.com/itsHenry35/ledu/commit/8dc935cbaf8ada4d26f2f5306f2b3307fac8d4b1))
* remove unnecessary return statement ([37bf397](https://github.com/itsHenry35/ledu/commit/37bf397c9686971da48108472e5ddb49b00cb31d))
* remove unnecessary return statement ([37bf397](https://github.com/itsHenry35/ledu/commit/37bf397c9686971da48108472e5ddb49b00cb31d))
* remove unnecessary return statement ([5ce13d1](https://github.com/itsHenry35/ledu/commit/5ce13d10be24ec219c06db4c2504e605750f0115))
* remove unnecessary whitespace ([a2abb90](https://github.com/itsHenry35/ledu/commit/a2abb90a56c13c1a56dbf748699df8460a684b47))
* remove unnecessary whitespace ([facc29c](https://github.com/itsHenry35/ledu/commit/facc29c0ece47b8b60524b1aa5cad9fe5fba51b9))
* remove unnecessary whitespace ([facc29c](https://github.com/itsHenry35/ledu/commit/facc29c0ece47b8b60524b1aa5cad9fe5fba51b9))
* remove unnecessary whitespace ([f1c82ae](https://github.com/itsHenry35/ledu/commit/f1c82ae5d9ad8df396c866d10c851f969e0c7cdd))
* remove unused global variable ([71aaa62](https://github.com/itsHenry35/ledu/commit/71aaa62ce31b6cb4f01cc0e5d1dd8d0843e16285))
* replace multiple `==` checks with `in` ([2f878a0](https://github.com/itsHenry35/ledu/commit/2f878a0e47ea5748d74b0d288d031f47ba1b3df7))
* replace multiple `==` checks with `in` ([d8ea79f](https://github.com/itsHenry35/ledu/commit/d8ea79fc3865eab5d40440933e207611a32ec42e))
* rewrite all code ([cd241ab](https://github.com/itsHenry35/ledu/commit/cd241ab2cf921b22435a52d696df643184cc6016))
* use identity check for comparison to a singleton ([0216d95](https://github.com/itsHenry35/ledu/commit/0216d95d4d0d531d8c8bb5d7a2f1d781d7467f87))


### Performance Improvements

* only open aria2 process at first run ([2076d9c](https://github.com/itsHenry35/ledu/commit/2076d9cf86ed646f03536dbd32ded49ff596d46c))


### CI

* actions build debug bin ([6dd3c02](https://github.com/itsHenry35/ledu/commit/6dd3c02c3269b7820177bd718f45ab36aa5bb7f0))
* add .deepsource.toml ([f696e94](https://github.com/itsHenry35/ledu/commit/f696e94b340a24a548f3b0334e0a3986a6dec6e2))
* auto merge only when release ([0b077fd](https://github.com/itsHenry35/ledu/commit/0b077fd5d7bfa46d16516049a222b52f29b5bc3e))
* auto merge release ([74dcaef](https://github.com/itsHenry35/ledu/commit/74dcaef551f825db67da6b598eeb20c197f918d0))
* build macos intel ([16c05cd](https://github.com/itsHenry35/ledu/commit/16c05cd5ee0b2e0b1d468dd63b6b0e910818dccd))
* build with 3.8.10 to try with windows 7 ([ab03805](https://github.com/itsHenry35/ledu/commit/ab03805eee953c1b183fbcdf4756c01da1f6a23f))
* Build with MacOS 13 ([5f4de1d](https://github.com/itsHenry35/ledu/commit/5f4de1d8a1d2236a248c82741f4ad3e41fa81457))
* don't move macos folder and fix windows build ([260fc6e](https://github.com/itsHenry35/ledu/commit/260fc6e57acc7daeec4e1d5fdc9d47bc7a6726c5))
* don't run debug when changelog modified [skip ci] ([d9b3e4a](https://github.com/itsHenry35/ledu/commit/d9b3e4aa48f85151a041f658d05810ff4406c70c))
* don't run github pages automatically ([77d6b9c](https://github.com/itsHenry35/ledu/commit/77d6b9ca9f973ab22f517315bf1f89b04b36e1be))
* error debug aria2c path ([2b9e4b6](https://github.com/itsHenry35/ledu/commit/2b9e4b621b20074e9ffc0dccf79118e3ddcc6c6d))
* fix another wrong usage ([f4cc16d](https://github.com/itsHenry35/ledu/commit/f4cc16d3f38f9721a80dbe2d27e6d85bc2987810))
* fix auto merge ([83386a9](https://github.com/itsHenry35/ledu/commit/83386a916809421c2c41d93563b158ee089a4a8f))
* fix broken CI because of empty version number ([d984210](https://github.com/itsHenry35/ledu/commit/d984210a8bb9eff59a159a6ede816fee4c8d2374))
* Fix for duplicate name [skip ci] ([cdfb0f7](https://github.com/itsHenry35/ledu/commit/cdfb0f77cbe760024e2ff0f4047fa5c4d0b975a9))
* fix release error ([0dbaba5](https://github.com/itsHenry35/ledu/commit/0dbaba56e527110e0d87574bf7406a02de7e514c))
* fix windows syntax error ([a7261ec](https://github.com/itsHenry35/ledu/commit/a7261ec91e612018a749a3a46c5bfaca9c38d467))
* fix wrong release tag and name ([80cd015](https://github.com/itsHenry35/ledu/commit/80cd015d2f3cddecbf3fd3696904b87129a11152))
* include commit number in the debug binary ([dd7442f](https://github.com/itsHenry35/ledu/commit/dd7442f8b39086de8745c35cd3ec20157e1cfe22))
* only run actions when release published to avoid running three times [skip ci] ([d9004f4](https://github.com/itsHenry35/ledu/commit/d9004f4430a66cfdcf0c4bbb05bb56a74bf20f23))
* only upload to release when first released ([7eb05d2](https://github.com/itsHenry35/ledu/commit/7eb05d2c324dc7ecb78354c7548b274465312f6a))
* release add version number ([2d6cb19](https://github.com/itsHenry35/ledu/commit/2d6cb19c3ad14f050d8e0c9b004be2f03e6eee62))
* release macos intel [skip ci] ([d8e7ee7](https://github.com/itsHenry35/ledu/commit/d8e7ee71c9e0cf95bf928cc1de080929ae661d38))
* release manually ([607c5d8](https://github.com/itsHenry35/ledu/commit/607c5d830b58135eec00f15e720319fbb4a76f28))
* remove auto merge ([d0c53e9](https://github.com/itsHenry35/ledu/commit/d0c53e9aac32af335606a85932b4b5fa56fd7d18))
* rename main.yml to build.yml ([1da8f39](https://github.com/itsHenry35/ledu/commit/1da8f39c350553f2e6914d50f40c3216fb5093f2))
* run release again when changelog changed ([a453516](https://github.com/itsHenry35/ledu/commit/a453516b5972da1a61357bd8f58474d842c22bec))
* simplify code ([1d4ce1a](https://github.com/itsHenry35/ledu/commit/1d4ce1a64e5576f3e8ef48b02f5505f7d36340b0))
* sync to release [skip ci] ([974a390](https://github.com/itsHenry35/ledu/commit/974a390d462a9d9c957f0c27b2804c9d7b61110b))
* upload debug binary for MacOS ([9acb393](https://github.com/itsHenry35/ledu/commit/9acb3934ad293a5eee391667ced536e3d277754f))
* use console for debug version ([09613ba](https://github.com/itsHenry35/ledu/commit/09613bab09818b5358b7054332be637bd2426d10))
* use ubuntu 20.04 for better compatibility ([ac0b268](https://github.com/itsHenry35/ledu/commit/ac0b2689a981d9ed03ffc5599139ec1c73b35657))
* wrong filename ([561c5f2](https://github.com/itsHenry35/ledu/commit/561c5f25ba2681a8a64a05a9be1d1b33a2e95bfb))

## [2.3.1](https://github.com/itsHenry35/ledu/compare/v2.3.0...v2.3.1) (2025-01-21)


### Bug Fixes

* also fix unexpected response for record_mode [skip ci] ([53a5d8c](https://github.com/itsHenry35/ledu/commit/53a5d8c6f546f13e395d284679785bf47f6fd786))

## [2.3.0](https://github.com/itsHenry35/ledu/compare/v2.2.2...v2.3.0) (2025-01-21)


### Features

* avoid path permission denials ([cbd1516](https://github.com/itsHenry35/ledu/commit/cbd1516cc3af6669bf8be0dc7c432f2b02190a89))


### Bug Fixes

* aria2 override params ([005fe9c](https://github.com/itsHenry35/ledu/commit/005fe9c119680c7c66cbb4935f647db3b428d3d4))
* sometimes video_data doesn't exist ([be7ab83](https://github.com/itsHenry35/ledu/commit/be7ab83fffd61d7cd78fad3af9bc6f26d4ac99e7))
* undefined var when exiting ([1f15fa2](https://github.com/itsHenry35/ledu/commit/1f15fa2dff45318455bb65aab25baa129071d231))


### CI

* Fix for duplicate name [skip ci] ([57f1282](https://github.com/itsHenry35/ledu/commit/57f1282490fd720a085952940416bc3a32bf765c))

## [2.2.2](https://github.com/itsHenry35/ledu/compare/v2.2.1...v2.2.2) (2024-09-29)


### CI

* release macos intel [skip ci] ([8a50cb9](https://github.com/itsHenry35/ledu/commit/8a50cb9ef85ca95044a051831aec7e5c3a23c0c7))

## [2.2.1](https://github.com/itsHenry35/ledu/compare/v2.2.0...v2.2.1) (2024-09-29)


### CI

* build macos intel ([d730cd7](https://github.com/itsHenry35/ledu/commit/d730cd753766a549d80283e6e9613be7634f0012))
* build with 3.8.10 to try with windows 7 ([6ca974b](https://github.com/itsHenry35/ledu/commit/6ca974bec7d4d713cb198d4c004241d66b7b41e3))
* Build with MacOS 13 ([ae18c60](https://github.com/itsHenry35/ledu/commit/ae18c60e6b57252176c04f0f5608f649559de080))
* simplify code ([ea94e6b](https://github.com/itsHenry35/ledu/commit/ea94e6b64dfe986f9298e4eaef8804a434580fa1))
* sync to release [skip ci] ([49b1e5a](https://github.com/itsHenry35/ledu/commit/49b1e5a5cf653da73b61e306651d8e5eb71bd899))

## [2.2.0](https://github.com/itsHenry35/ledu/compare/v2.1.1...v2.2.0) (2024-09-28)


### Features

* support non-override ([3dacc63](https://github.com/itsHenry35/ledu/commit/3dacc6397d1f18018146bf55bd8f7594edc1ae5a))


### Code Refactoring

* add newline at end of file ([398a91b](https://github.com/itsHenry35/ledu/commit/398a91b28b2f5a7b9a904f7c3d6608f35c8fa7a0))
* refactor `if` expression ([7431ee2](https://github.com/itsHenry35/ledu/commit/7431ee26a26115b4ac83e4c72b76958b9e28d79e))
* refactor useless `else` block in the loop ([384edad](https://github.com/itsHenry35/ledu/commit/384edad57f691a1bb98cbf5b68633341372ef119))
* remove unnecessary whitespace ([8cf9274](https://github.com/itsHenry35/ledu/commit/8cf9274bbd8cb6632d558691e883c640565a4a08))
* remove unused global variable ([cada944](https://github.com/itsHenry35/ledu/commit/cada944cb6f93d4f667f216fc90a713b07637342))
* replace multiple `==` checks with `in` ([7c6712b](https://github.com/itsHenry35/ledu/commit/7c6712bb297d36ff3920432bc70c271dc2ae60bf))
* use identity check for comparison to a singleton ([c7fd146](https://github.com/itsHenry35/ledu/commit/c7fd1465101c8846f3ebaed7f496c02e1734205d))

## [2.1.1](https://github.com/itsHenry35/ledu/compare/v2.1.0...v2.1.1) (2024-09-16)


### Bug Fixes

* unable to download in linux ([a7663dd](https://github.com/itsHenry35/ledu/commit/a7663dd77c424e37b6d5cff0e1d8cd0ec67f7f15))

## [2.1.0](https://github.com/itsHenry35/ledu/compare/v2.0.1...v2.1.0) (2024-09-16)


### Features

* don't pop up aria2 window ([43f713e](https://github.com/itsHenry35/ledu/commit/43f713ea212d5d8b694250e730b9fe0a4e6a83d5))
* support 'COMBINE_SMALL_CLASS_MODE' ([1026525](https://github.com/itsHenry35/ledu/commit/1026525c7722c2be08862301beec8b4896b85b5a))

## [2.0.1](https://github.com/itsHenry35/ledu/compare/v2.0.0...v2.0.1) (2024-02-07)


### Docs

* improve error feedback ([a2ef373](https://github.com/itsHenry35/ledu/commit/a2ef373f64cf10ecbebb09fc7a6ac7371ed29c2e))

## [2.0.0](https://github.com/itsHenry35/ledu/compare/v1.6.1...v2.0.0) (2024-02-07)


### ⚠ BREAKING CHANGES

* import aria2c from motrix

### Features

* import aria2c from motrix ([c432ff3](https://github.com/itsHenry35/ledu/commit/c432ff3a957e8be6117dfee4717535664ebab93b))
* new url place support and support for "无回放"courses ([149f762](https://github.com/itsHenry35/ledu/commit/149f7626bd90392b05afd44af301c40475d89e53))


### CI

* error debug aria2c path ([33275cf](https://github.com/itsHenry35/ledu/commit/33275cfb2963493eba834fbe1929bb962f0dc3e8))

## [1.6.1](https://github.com/itsHenry35/ledu/compare/v1.6.0...v1.6.1) (2023-12-24)


### Code Refactoring

* convert string with anomalous backslash into a raw string ([1a068b6](https://github.com/itsHenry35/ledu/commit/1a068b6027457df31b4c01b5297c380a8c696aa6))
* convert string with anomalous backslash into a raw string ([1a068b6](https://github.com/itsHenry35/ledu/commit/1a068b6027457df31b4c01b5297c380a8c696aa6))
* convert string with anomalous backslash into a raw string ([8523c36](https://github.com/itsHenry35/ledu/commit/8523c36b5be37618cd3c6ea49b17a93e420d2cc6))
* import packages in separate lines ([a96afad](https://github.com/itsHenry35/ledu/commit/a96afadff2e160890ac17878340d07259295af4a))
* refactor unnecessary `else` / `elif` when `if` block has a `raise` statement ([d1a127b](https://github.com/itsHenry35/ledu/commit/d1a127b5cd9de8874cc9ef9e29acd8b77001705e))
* refactor unnecessary `else` / `elif` when `if` block has a `raise` statement ([d1a127b](https://github.com/itsHenry35/ledu/commit/d1a127b5cd9de8874cc9ef9e29acd8b77001705e))
* refactor unnecessary `else` / `elif` when `if` block has a `raise` statement ([d213fbc](https://github.com/itsHenry35/ledu/commit/d213fbcd81ee6b96bb81745f0334b16072586a60))
* refactor unnecessary `else` / `elif` when `if` block has a `return` statement ([6feb186](https://github.com/itsHenry35/ledu/commit/6feb1866fd630928f7e9480044d00387b6712692))
* remove unnecessary return statement ([c8b38cf](https://github.com/itsHenry35/ledu/commit/c8b38cf83424cb6237321f2d89b4fe8782465a91))
* remove unnecessary return statement ([c8b38cf](https://github.com/itsHenry35/ledu/commit/c8b38cf83424cb6237321f2d89b4fe8782465a91))
* remove unnecessary return statement ([79bfb7e](https://github.com/itsHenry35/ledu/commit/79bfb7edb68af559a7d4fbe61b9ecf3df21ff396))
* remove unnecessary whitespace ([1c430fe](https://github.com/itsHenry35/ledu/commit/1c430fe485bf871a25e956addc2030be22ff59b7))
* remove unnecessary whitespace ([1c430fe](https://github.com/itsHenry35/ledu/commit/1c430fe485bf871a25e956addc2030be22ff59b7))
* remove unnecessary whitespace ([74f1e9b](https://github.com/itsHenry35/ledu/commit/74f1e9bf086b2501b45a5334e0fcd96035d80a41))
* replace multiple `==` checks with `in` ([026e5b2](https://github.com/itsHenry35/ledu/commit/026e5b2ba9dbde7d4beefb0d61ad013dfe7f74f2))


### Performance Improvements

* only open aria2 process at first run ([7b1ef99](https://github.com/itsHenry35/ledu/commit/7b1ef993282b77df961ae8c712c2b4db7cc1f5c4))


### CI

* add .deepsource.toml ([ba623cb](https://github.com/itsHenry35/ledu/commit/ba623cb5a52f907182956c10bfb935b79727172f))

## [1.6.0](https://github.com/itsHenry35/ledu/compare/v1.5.2...v1.6.0) (2023-11-05)


### Features

* add subject name to the downloaded files ([d9ec038](https://github.com/itsHenry35/ledu/commit/d9ec03851fc440ba00092587113fc078d0502b7a))
* pause / resume button ([832eef8](https://github.com/itsHenry35/ledu/commit/832eef8d4300a6f793cdfdecd5ce91ffcbd7f13d))
* show progress (eg. 2/4 downloaded) ([890dfbd](https://github.com/itsHenry35/ledu/commit/890dfbdb515e4c69bbd58d1c8526884d0ef0d935))

## [1.5.2](https://github.com/itsHenry35/ledu/compare/v1.5.1...v1.5.2) (2023-11-03)


### CI

* fix broken CI because of empty version number ([25b18a9](https://github.com/itsHenry35/ledu/commit/25b18a9462ee49e2de23ae9624ab2bebe9acd6c2))
* rename main.yml to build.yml ([77c45b8](https://github.com/itsHenry35/ledu/commit/77c45b82ec61f372ef78868de57284e95a969359))

## [1.5.1](https://github.com/itsHenry35/ledu/compare/v1.5.0...v1.5.1) (2023-11-03)


### Bug Fixes

* fix the error if the class hasn't started yet ([4eb62fb](https://github.com/itsHenry35/ledu/commit/4eb62fbeea79f4359366ab375be4f7773822eb0f))

## [1.5.0](https://github.com/itsHenry35/ledu/compare/v1.4.1...v1.5.0) (2023-09-29)


### Features

* replace illegal characters ([829bd32](https://github.com/itsHenry35/ledu/commit/829bd3299e9f62860efae82bd90ed76880996305))


### Bug Fixes

* fix logical error when error password occurs ([91f729b](https://github.com/itsHenry35/ledu/commit/91f729b01fed84490b7b925aab77d2c48127769e))


### CI

* remove auto merge ([12d0347](https://github.com/itsHenry35/ledu/commit/12d034776b2a8488f2655e17c2f52f624cfe90ff))

## [1.4.1](https://github.com/itsHenry35/ledu/compare/v1.4.0...v1.4.1) (2023-09-24)


### Bug Fixes

* syntax error powershell varieble ([5af471b](https://github.com/itsHenry35/ledu/commit/5af471b4fa5f7e061810c6284a96aa044508353c))


### CI

* don't move macos folder and fix windows build ([04980f6](https://github.com/itsHenry35/ledu/commit/04980f64652ba0f975bf7ab850a9c8f9e515615a))
* fix another wrong usage ([bdbc5e4](https://github.com/itsHenry35/ledu/commit/bdbc5e4190806d39d59a8c5697637fcac44a98d7))
* fix auto merge ([4b50ff9](https://github.com/itsHenry35/ledu/commit/4b50ff9dabf15c72cc30f83c628ba4b5039e68e0))
* fix windows syntax error ([81bae48](https://github.com/itsHenry35/ledu/commit/81bae48b7e23a7d55375fe504b4e458fe9d04e46))
* include commit number in the debug binary ([8660daa](https://github.com/itsHenry35/ledu/commit/8660daa279a5bfee6b142b5312a6509463cdf8a0))
* release add version number ([279392d](https://github.com/itsHenry35/ledu/commit/279392d2e0f2fe59a2d0ead2cf5b7a3fa61eec86))
* upload debug binary for MacOS ([b159f49](https://github.com/itsHenry35/ledu/commit/b159f497fc0fc899cc3eb084547ec9c744ae2193))
* use console for debug version ([ffb18ab](https://github.com/itsHenry35/ledu/commit/ffb18abf7994fe6fd789871ef146e295e790a0bc))
* wrong filename ([299c3b9](https://github.com/itsHenry35/ledu/commit/299c3b90213cbecd0aebe6a9eba540c8d06830a9))

## [1.4.0](https://github.com/itsHenry35/ledu/compare/v1.3.0...v1.4.0) (2023-09-23)


### Features

* support scrollbar ([62aa411](https://github.com/itsHenry35/ledu/commit/62aa41162de93f24cdcf060d34e4a2bae707bb46))


### Bug Fixes

* Chinese typo [skip ci] ([b63ea70](https://github.com/itsHenry35/ledu/commit/b63ea7041fd4774cb54aaebc8c98b75272347ab0))


### Code Refactoring

* code refactor with idea [skip CI] ([e82e822](https://github.com/itsHenry35/ledu/commit/e82e8229fd3a76fc25e8426334e07f24a91bb902))
* refactor for code regulation with pycharm ([38e0306](https://github.com/itsHenry35/ledu/commit/38e0306a52ab9fcefee7111e95a5495777100410))


### CI

* don't run debug when changelog modified [skip ci] ([32ea7e7](https://github.com/itsHenry35/ledu/commit/32ea7e7e451a16b52f3387881596d8be9a5713b2))
* only run actions when release published to avoid running three times [skip ci] ([aaded38](https://github.com/itsHenry35/ledu/commit/aaded38c4ba15ef58c5dd7a1a88c5959e3cd292e))

## [1.3.0](https://github.com/itsHenry35/ledu/compare/v1.2.2...v1.3.0) (2023-07-04)


### Features

* ask the user whether to open error reporting website ([5895af6](https://github.com/itsHenry35/ledu/commit/5895af6d4bba750341fa5ca8f4199abccda6347b))
* support multi course downloading and custom download path ([70ba0b1](https://github.com/itsHenry35/ledu/commit/70ba0b1bc98156c26094c356515c23d9513b73c1))

## [1.2.2](https://github.com/itsHenry35/ledu/compare/v1.2.1...v1.2.2) (2023-06-27)


### Bug Fixes

* double quote to avoid usernames with a space on Windows ([21c992d](https://github.com/itsHenry35/ledu/commit/21c992db50fa820d25606da93865440250ca732e))

## [1.2.1](https://github.com/itsHenry35/ledu/compare/v1.2.0...v1.2.1) (2023-06-22)


### CI

* fix wrong release tag and name ([a3a06cc](https://github.com/itsHenry35/ledu/commit/a3a06cc337b5fe0d60e222b54b841a1607290acd))

## [1.2.0](https://github.com/itsHenry35/ledu/compare/v1.1.0...v1.2.0) (2023-06-22)


### Features

* better layout ([f507c87](https://github.com/itsHenry35/ledu/commit/f507c87cc19361f61b1d57cdafa14411d6b2cd86))
* support dynamic window resizing ([6a1b5f8](https://github.com/itsHenry35/ledu/commit/6a1b5f8a75ab6f811b40ee9c368478aead817609))


### Bug Fixes

* error downloading after switching back from sms ([fc1c108](https://github.com/itsHenry35/ledu/commit/fc1c10865ee2c9ac8ae19dec0c7c9571a3ee1c08))
* sms not defined error while closing ([e6e9041](https://github.com/itsHenry35/ledu/commit/e6e9041422e957811fbea92bcb7e6e85fa2200ad))
* Switching between sms and pwd may trigger loop ([7a42a70](https://github.com/itsHenry35/ledu/commit/7a42a7099db9bbd245a391ec9e51366840b7d9fa))

## [1.1.0](https://github.com/itsHenry35/ledu/compare/v1.0.3...v1.1.0) (2023-06-14)


### Features

* add error handling and error reporting ([39c823d](https://github.com/itsHenry35/ledu/commit/39c823d0d113f531152100533db3949a32f2f10a))


### Code Refactoring

* rewrite all code ([9f9a792](https://github.com/itsHenry35/ledu/commit/9f9a792f04c2ef555a069e6eeeef03676569e384))

## [1.0.3](https://github.com/itsHenry35/ledu/compare/v1.0.2...v1.0.3) (2023-05-14)


### CI

* use ubuntu 20.04 for better compatibility ([e6da0b8](https://github.com/itsHenry35/ledu/commit/e6da0b8428a171f426b3ac33ed126ba75897e408))

## [1.0.2](https://github.com/itsHenry35/ledu/compare/v1.0.1...v1.0.2) (2023-03-22)


### CI

* auto merge release ([38d5899](https://github.com/itsHenry35/ledu/commit/38d58995fd79b6baa69c1b07e8dac3930e7754a4))
* fix release error ([37b3e31](https://github.com/itsHenry35/ledu/commit/37b3e3114e6fb67ac14b1227e0560cc0f058ac82))
* run release again when changelog changed ([1380271](https://github.com/itsHenry35/ledu/commit/13802714d03cf22b0832933e0ce8482ad7cc03fb))

## [1.0.1](https://github.com/itsHenry35/ledu/compare/v1.0.0...v1.0.1) (2023-03-22)


### Bug Fixes

* do not commit complied python files ([d5f6a57](https://github.com/itsHenry35/ledu/commit/d5f6a57678453ea1278b0f4a122bc7b6b14899f1))


### CI

* actions build debug bin ([01fec31](https://github.com/itsHenry35/ledu/commit/01fec319a14881aa9ed79c4e57f44f0533d7a2d3))
* don't run github pages automatically ([5cee003](https://github.com/itsHenry35/ledu/commit/5cee0036d98e0eeeeaa61ece3c6d53004ae68d59))
* only upload to release when first released ([5217103](https://github.com/itsHenry35/ledu/commit/521710367f77001aa25bfa39fb97fa4d1ec9aba6))

## 1.0.0 (2023-03-22)


### Features

* A button to open the downloading folder has been added ([c802b2b](https://github.com/itsHenry35/ledu/commit/c802b2be9be707b5a33ffb699ba5357a7d8a2ec7))


### Bug Fixes

* Progress will be 99 percent even if the download has completed ([c802b2b](https://github.com/itsHenry35/ledu/commit/c802b2be9be707b5a33ffb699ba5357a7d8a2ec7))
