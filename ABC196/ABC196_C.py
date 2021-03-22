# 入力
N = input()

N_length = len(N)

# 数列の桁数が偶数ならば
if N_length % 2 == 0:
    # 数列を前半と後半に分ける
    front = N[:(N_length//2)]
    back = N[(N_length//2):]
    # 前半よりも後半の数の方が大きければ前半の数を出力、そうでなければ後半の数を出力
    if int(front) <= int(back):
        print(front)
    else:
        print(int(front)-1)
# 数列の桁数が偶数でないならば
else:
    # 数列の桁数が1なら0、そうでないなら桁数を一つ下げ偶数にし、
    # 前半と後半で文字列が等しくなる最大の数を出力
    if N_length == 1:
        print(0)
    else:
        print("9"*(N_length//2))

"""
<header>
      <div class="header-container">
        <div class="header-logo">Well-child-Space</div>
        <div class="header-list">
        <ul>
          <li>ログアウト</li>
          <li>プロフィール</li>
          <li>お気に入り</li>
          <li>検索</li>
        </ul>
        </div>
    </header>

    * {
     margin: 0px;
     padding: 0px;
 }

 header {
    background-color: #ffb4b4;
    color: rgb(253, 253, 253);
    height: 90px;
    
 }

 .header-container {
    width: 1450px;
    margin: 0 auto;

 }


 .header-logo {
     font-size: 36px;
     float: left;
     padding: 15px 10px; 
     height: 60px; 
 }


 .header-logo:hover {
     background-color: #f390a0;
 }

 .header-list li {
     list-style: none;
     float: right;
     padding: 33px 20px;
 }

 .header-list li:hover {
    background-color: #f390a0;
 }

 h2 {
    color: rgb(250, 127, 127);
    font-size: 50px;
    font-family: serif;
 }
"""