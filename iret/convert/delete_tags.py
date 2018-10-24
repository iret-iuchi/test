# coding: utf-8
import io
from html.parser import HTMLParser

class MyHtmlStripper(HTMLParser):
    def __init__(self, s):
        super().__init__()
        self.sio = io.StringIO()
        self.feed(s)

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        self.sio.write(data)

    @property
    def value(self):
        return self.sio.getvalue()


s2 = """
<h3>３【事業の内容】</h3> <p style="text-align: left"> </p> <p style="text-align: left; text-indent: 12px">当社は、銀行持株会社として、銀行持株会社、銀行、長期信用銀行、証券専門会社及びその他銀行法により子会社とすることができる会社の経営管理ならびにこれに附帯する業務を行うことを事業目的としております。</p> <p style="text-align: left; text-indent: 12px">「みずほフィナンシャルグループ」（以下、当社グループ）は、当社、連結子会社159社及び持分法適用関連会社21社等で構成され、銀行業務、信託業務、証券業務、その他の金融サービスに係る業務を行っております。</p> <p style="text-align: left; text-indent: 13.3299999237061px">当連結会計年度末における当社グループの組織を事業系統図によって示すと以下のとおりであります。</p> <p style="text-align: left"> </p> <p style="text-align: center">事業系統図</p> <p style="text-align: right">（平成26年３月31日現在）</p> <p style="text-align: center"> <img style="height: 710.369995117188px; width: 644.004028320313px" src="images/0101010_001.png" alt="0101010_001.png"/> </p> <p style="margin-left: 36px; text-align: left"> </p> <p style="text-align: left" class="style_pb_after"> </p> <p style="text-align: left">　当社は、平成26年６月24日付で委員会設置会社へ移行いたしました。平成26年６月24日時点の事業系統図は以下のとおりであります。</p> <p style="text-align: left"> </p> <p style="text-align: center">事業系統図</p> <p style="text-align: right">（平成26年６月24日現在）</p> <p style="text-align: center"> <img style="height: 712.409973144531px; width: 643.998229980469px" src="images/0101010_002.png" alt="0101010_002.png"/> </p> <p style="text-align: left"> </p> <p style="text-align: left" class="style_pb_after"> </p> <p style="text-align: left">　当社及び当社の主な関係会社を事業セグメント別に区分いたしますと、下記のとおりとなります。</p> <p style="margin-left: 24px; text-align: left">株式会社みずほ銀行（連結）：</p> <p style="margin-left: 36.0699996948242px; text-align: left">株式会社みずほ銀行、みずほ信用保証株式会社、確定拠出年金サービス株式会社、みずほファクター株式会社、みずほキャピタル株式会社、ユーシーカード株式会社、みずほ第一フィナンシャルテクノロジー株式会社、瑞穂銀行（中国）有限公司、PT. Bank Mizuho Indonesia、Mizuho Bank Nederland N.V.、Mizuho Bank (USA)、Mizuho Capital Markets Corporation、株式会社オリエントコーポレーション、Joint Stock Commercial Bank for Foreign Trade of Vietnam</p> <p style="margin-left: 24px; text-align: left">みずほ信託銀行株式会社（連結）：</p> <p style="margin-left: 36.0699996948242px; text-align: left">みずほ信託銀行株式会社、みずほ信不動産販売株式会社、Mizuho Trust &amp; Banking Co.(USA)、Mizuho Trust &amp; Banking (Luxembourg) S.A.、日本株主データサービス株式会社、日本ペンション・オペレーション・サービス株式会社</p> <p style="margin-left: 24px; text-align: left">みずほ証券株式会社（連結）：</p> <p style="margin-left: 36.0699996948242px; text-align: left">みずほ証券株式会社、新光投信株式会社、Mizuho International plc、Mizuho Securities USA Inc.、Mizuho Securities Asia Limited、Mizuho Bank (Switzerland) Ltd</p> <p style="margin-left: 24px; text-align: left">その他：</p> <p style="margin-left: 36px; text-align: left">株式会社みずほフィナンシャルグループ、資産管理サービス信託銀行株式会社、みずほ投信投資顧問株式会社、ＤＩＡＭアセットマネジメント株式会社、みずほ総合研究所株式会社、みずほ情報総研株式会社、株式会社みずほフィナンシャルストラテジー、株式会社みずほプライベートウェルスマネジメント</p> <p style="margin-left: 12px; text-align: left"> </p> <p style="text-align: left">　なお、当社は、有価証券の取引等の規制に関する内閣府令第49条第２項に規定する特定上場会社等に該当しており、これにより、インサイダー取引規制の重要事実の軽微基準については連結ベースの数値に基づいて判断することとなります。</p> <p style="text-align: left"> </p>
"""

print(MyHtmlStripper(s2).value)
