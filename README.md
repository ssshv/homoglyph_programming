# homoglyph_programming
ホモグリフ攻撃の実例


## homoglyph_code
- 攻撃対象を(php_hw)[https://github.com/IldarDavletyarov/php_hw]とする。
- /7/index.phpの23行目の変数$commandのaをaのホモグリフであるа(U+0430)に置換する。
- ホモグリフに置換することで、escapeshellcmd関数の実行を回避できるために、後で実行されるexec関数においてOSコマンドインジェクションが可能となる。


```
$command = "ping {$address} -c 3  -W 1 -q ";
$commаnd = escapeshellcmd($command);
$string = exec($command, $arr);
```

## homogly_file
- 攻撃対象を(image_encryption)[https://github.com/PM25/image_encryption]とする。
- encrypt.pyというファイルで以下のように自作モジュールを使用している。

```
from mylib import utils
from mylib.crypto import MyCrypto

import argparse
import numpy as np
from PIL import Image
```

- crypto.pyの先頭のcをcのホモグリフであるс(U+0441)に変えたсrypto.py(ホモグリフファイル)を用意する．
- 内容は元になったcrypto.pyに実行したいコードを追加(ホモグリフファイルの8行目)
- encrypt.pyのimport宣言`from mylib.crypto import MyCrypto`のcをホモグリフに変更
  - 宣言順も変更することで、Githubでは新規に追加された行として検出されて、ホモグリフへの変更をばれにくくしている。
  
  
```
import argparse
import numpy as np
from PIL import Image

from mylib.сrypto import MyCrypto
from mylib import utils
from mylib import getinfo
```


