"""All site text in three languages. build.py renders it into static pages.

Facts used here come from the company's own website (gzltzdh.cn), its brochure and public
registration records. Customer names are not used. Edit text here, then run: python3 _src/build.py
"""

LANGS = ["en", "vi", "zh"]
LANG_LABEL = {"en": "EN", "vi": "VI", "zh": "中文"}
HTML_LANG = {"en": "en", "vi": "vi", "zh": "zh-Hans"}

PHONE = "+86 133 0220 3440"
PHONE_TEL = "+8613302203440"
EMAIL = "sales@longtengautomation.com"

T = {
    "brand_sub": {"en": "Guangzhou Longteng Automation Equipment Co., Ltd.",
                  "vi": "Công ty TNHH Thiết bị Tự động hóa Longteng Quảng Châu",
                  "zh": "广州龙腾自动化设备有限公司"},
    "nav": {"en": ["Home", "Solutions", "Equipment", "Projects", "About", "Contact"],
            "vi": ["Trang chủ", "Giải pháp", "Thiết bị", "Dự án", "Giới thiệu", "Liên hệ"],
            "zh": ["首页", "行业方案", "设备产品", "项目案例", "关于我们", "联系我们"]},
    "cta": {"en": "Request a quote", "vi": "Yêu cầu báo giá", "zh": "获取报价"},
    "topbar": {"en": "Custom automation for factories in Vietnam · Guangzhou is 2 hours' flight from Hanoi",
               "vi": "Tự động hóa theo yêu cầu cho nhà máy tại Việt Nam · Quảng Châu cách Hà Nội 2 giờ bay",
               "zh": "为越南工厂定制自动化设备 · 广州至河内航程约 2 小时"},
    "hero_tag": {"en": "Assembly · Testing · Vision inspection · Laser welding · Hot stamping",
                 "vi": "Lắp ráp · Kiểm tra · Kiểm tra bằng camera · Hàn laser · Ép nhũ nóng",
                 "zh": "装配 · 检测 · 视觉检测 · 激光焊接 · 烫印"},
    "hero_h1": {"en": "Custom assembly and test lines, built around your product",
                "vi": "Dây chuyền lắp ráp và kiểm tra tự động, thiết kế theo sản phẩm của bạn",
                "zh": "围绕您的产品，定制装配与检测整线"},
    "hero_p": {"en": "Non-standard automation for small appliances, personal-care products, electronics, EV components, locks and packaging — designed, built and tested in Guangzhou, installed and supported at your factory.",
               "vi": "Thiết bị tự động hóa phi tiêu chuẩn cho điện gia dụng nhỏ, sản phẩm chăm sóc cá nhân, điện tử, linh kiện xe điện, khóa và bao bì — thiết kế, chế tạo và chạy thử tại Quảng Châu, lắp đặt và hỗ trợ tại nhà máy của bạn.",
               "zh": "面向小家电、个护电器、电子、新能源汽车零部件、锁具与包装行业的非标自动化设备：在广州设计、制造并完成出厂测试，到您的工厂安装调试并提供售后服务。"},
    "hero_btn2": {"en": "See our equipment", "vi": "Xem thiết bị", "zh": "查看设备"},
    "stats": {"en": [("2019", "Founded in Guangzhou"), ("National", "High-Tech Enterprise (2025)"), ("9", "Granted patents"), ("35+", "Machine types delivered"), ("FAT", "Factory acceptance test before shipment")],
              "vi": [("2019", "Thành lập tại Quảng Châu"), ("Quốc gia", "Doanh nghiệp công nghệ cao (2025)"), ("9", "Bằng sáng chế được cấp"), ("35+", "Loại máy đã chế tạo"), ("FAT", "Nghiệm thu tại xưởng trước khi giao")],
              "zh": [("2019", "成立于广州"), ("国家级", "高新技术企业（2025）"), ("9 件", "授权专利"), ("35+", "已交付的设备类型"), ("FAT", "出厂前工厂验收")]},
    "sol_h": {"en": "Solutions by industry", "vi": "Giải pháp theo ngành", "zh": "行业方案"},
    "sol_sub": {"en": "Tell us your product and target output. We design the machine or the whole line around it.",
                "vi": "Hãy cho chúng tôi biết sản phẩm và sản lượng mục tiêu. Chúng tôi thiết kế máy hoặc cả dây chuyền theo đó.",
                "zh": "告诉我们您的产品与目标产能，我们据此设计单机或整线。"},
    "feat_h": {"en": "Featured projects", "vi": "Dự án tiêu biểu", "zh": "代表项目"},
    "how_h": {"en": "How we work", "vi": "Quy trình hợp tác", "zh": "合作流程"},
    "how_sub": {"en": "From your sample to a running line.", "vi": "Từ mẫu sản phẩm đến dây chuyền vận hành.", "zh": "从您的样品，到运行的产线。"},
    "steps": {"en": [("Sample & target", "Product, drawings, cycle time, output and budget."),
                     ("Concept & quote", "Process layout, 3D design and quotation."),
                     ("Build & FAT", "Built in our Guangzhou plant; witness the factory test on site or by video."),
                     ("Ship & install", "Shipped to Hai Phong or Ho Chi Minh City; our technicians install and commission."),
                     ("Support", "Operator training, remote diagnosis and a spare-parts kit.")],
              "vi": [("Mẫu & mục tiêu", "Sản phẩm, bản vẽ, nhịp sản xuất, sản lượng và ngân sách."),
                     ("Phương án & báo giá", "Bố trí quy trình, thiết kế 3D và báo giá."),
                     ("Chế tạo & FAT", "Chế tạo tại xưởng Quảng Châu; khách hàng chứng kiến nghiệm thu tại chỗ hoặc qua video."),
                     ("Vận chuyển & lắp đặt", "Giao đến Hải Phòng hoặc TP. Hồ Chí Minh; kỹ thuật viên lắp đặt và chạy thử."),
                     ("Hỗ trợ", "Đào tạo vận hành, chẩn đoán từ xa và bộ phụ tùng dự phòng.")],
              "zh": [("样品与目标", "产品、图纸、节拍、产能与预算。"),
                     ("方案与报价", "工艺布局、三维设计与报价。"),
                     ("制造与验收", "在广州工厂制造；客户可到场或通过视频见证出厂验收。"),
                     ("发运与安装", "发运至海防或胡志明市，技术人员到场安装调试。"),
                     ("售后支持", "操作培训、远程诊断与备件包。")]},
    "cta_band_h": {"en": "Have a product that needs automating?", "vi": "Bạn có sản phẩm cần tự động hóa?", "zh": "有需要自动化的产品？"},
    "cta_band_p": {"en": "Send us a photo, drawing or video of your product and process. We reply within one working day.",
                   "vi": "Gửi cho chúng tôi ảnh, bản vẽ hoặc video về sản phẩm và quy trình. Chúng tôi phản hồi trong vòng một ngày làm việc.",
                   "zh": "发来产品与工序的照片、图纸或视频，我们一个工作日内回复。"},
    "footer_rights": {"en": "All rights reserved.", "vi": "Bảo lưu mọi quyền.", "zh": "版权所有。"},
    "draft": {"en": "Draft for review — not yet published.", "vi": "Bản nháp để duyệt — chưa công bố.", "zh": "审阅草稿，尚未正式发布。"},
}

# ── industries ────────────────────────────────────────────────────────────
INDUSTRIES = [
    {"id": "appliances", "img": "site/hero-line.jpg",
     "t": {"en": "Small appliances & personal care", "vi": "Điện gia dụng nhỏ & chăm sóc cá nhân", "zh": "小家电与个护电器"},
     "d": {"en": "Hair dryers, shavers, trimmers, clippers and electric toothbrushes: riveting, press-fit, screw-driving, assembly lines, airtight, waterproof and life testing.",
           "vi": "Máy sấy tóc, máy cạo râu, máy tỉa, tông đơ và bàn chải điện: tán đinh, ép, bắt vít, dây chuyền lắp ráp, kiểm tra kín khí, chống nước và tuổi thọ.",
           "zh": "电吹风、剃须刀、鼻毛器、理发器、电动牙刷：铆接、压装、锁螺丝、组装线，以及气密、防水与寿命测试。"}},
    {"id": "vision", "img": "eq/vision-laser-marking.jpg",
     "t": {"en": "Electronics & vision inspection", "vi": "Điện tử & kiểm tra bằng camera", "zh": "电子与视觉检测"},
     "d": {"en": "CCD vision for defect detection, positioning, guided assembly and screw-driving, glue inspection and multi-material sorting; PCB soldering and component forming.",
           "vi": "Camera CCD phát hiện lỗi ngoại quan, định vị, lắp ráp và bắt vít theo camera, kiểm tra keo, phân loại vật liệu; hàn bo mạch và tạo hình linh kiện.",
           "zh": "CCD 视觉用于外观瑕疵检测、定位、视觉引导组装与锁螺丝、点胶检测和多物料分选；电路板焊接与元件整形。"}},
    {"id": "locks", "img": "eq/laser-line-overview.jpg",
     "t": {"en": "Locks & metal hardware", "vi": "Khóa & kim khí", "zh": "锁具与五金"},
     "d": {"en": "Laser welding, assembly and orbital riveting lines for smart-lock bodies and metal sub-assemblies.",
           "vi": "Dây chuyền hàn laser, lắp ráp và tán xoay cho thân khóa thông minh và cụm chi tiết kim loại.",
           "zh": "智能锁锁体与金属组件的激光焊接、组装与旋铆生产线。"}},
    {"id": "ev", "img": "eq/ptc-line-b.jpg",
     "t": {"en": "EV & automotive components", "vi": "Linh kiện ô tô & xe điện", "zh": "新能源汽车与汽车零部件"},
     "d": {"en": "Assembly and test lines for battery-protection PTC water heaters; hot stamping of automotive grilles.",
           "vi": "Dây chuyền lắp ráp và kiểm tra cụm sưởi nước PTC bảo vệ pin; ép nhũ nóng lưới tản nhiệt ô tô.",
           "zh": "电池保护 PTC 水发热包组装检测线；汽车进气格栅烫印。"}},
    {"id": "packaging", "img": "eq/mascara-cap-hot-stamping.jpg",
     "t": {"en": "Packaging & cosmetics", "vi": "Bao bì & mỹ phẩm", "zh": "化妆品包材与包装"},
     "d": {"en": "Automatic hot stamping, pad printing and laser marking for cosmetic caps and closures; blister welding and packing.",
           "vi": "Ép nhũ nóng, in tampon và khắc laser tự động cho nắp mỹ phẩm; hàn và đóng gói vỉ nhựa.",
           "zh": "化妆品瓶盖的自动烫印、移印与激光打标；吸塑焊接与包装。"}},
    {"id": "garment", "img": "site/workshop-1.jpg",
     "t": {"en": "Garment production", "vi": "May mặc", "zh": "服装生产"},
     "d": {"en": "Production-line equipment for garment factories; equipment already delivered and installed in Vietnam.",
           "vi": "Thiết bị dây chuyền cho nhà máy may; đã giao và lắp đặt tại Việt Nam.",
           "zh": "服装工厂生产线设备；已在越南交付并安装。"}},
]

# ── equipment catalogue (35 machines, names from the company's Chinese site) ──
CATS = [
    ("dryer", {"en": "Hair-dryer components", "vi": "Linh kiện máy sấy tóc", "zh": "电吹风零部件"}),
    ("shaver", {"en": "Shavers, trimmers & clippers", "vi": "Máy cạo râu, máy tỉa & tông đơ", "zh": "剃须刀、鼻毛器、剃毛器、理发器"}),
    ("brush", {"en": "Electric toothbrushes", "vi": "Bàn chải điện", "zh": "电动牙刷"}),
    ("test", {"en": "Life, performance & airtight testing", "vi": "Kiểm tra tuổi thọ, hiệu năng & độ kín khí", "zh": "寿命、性能与气密检测"}),
    ("elec", {"en": "Electronic components", "vi": "Linh kiện điện tử", "zh": "电子元件"}),
    ("stamp", {"en": "Hot stamping & marking", "vi": "Ép nhũ nóng & khắc dấu", "zh": "烫印与打标"}),
    ("line", {"en": "Complete production lines", "vi": "Dây chuyền hoàn chỉnh", "zh": "整线"}),
]

EQ = [
    ("dryer", None, "电吹风发热架基板鸡眼（铆钉）自动铆接设备", "Hair-dryer heater frame eyelet auto-riveting machine", "Máy tán khoen tự động cho đế khung nhiệt máy sấy tóc"),
    ("dryer", None, "电吹风分压电阻端子自动铆接设备", "Hair-dryer divider-resistor terminal auto-riveting machine", "Máy tán tự động đầu cốt điện trở phân áp máy sấy tóc"),
    ("dryer", None, "电吹风加热器电阻自动铆接设备", "Hair-dryer heater resistor auto-riveting machine", "Máy tán tự động điện trở bộ gia nhiệt máy sấy tóc"),
    ("dryer", None, "电吹风整流桥自动生产设备", "Hair-dryer rectifier bridge automatic production machine", "Máy sản xuất tự động cầu chỉnh lưu máy sấy tóc"),
    ("dryer", None, "电吹风整流翼组件自动组立设备", "Hair-dryer airflow vane assembly machine", "Máy lắp ráp tự động cụm cánh dẫn gió máy sấy tóc"),
    ("dryer", "dryer-fuse-cut-to-length.jpg", "电吹风温度保险管定长自动裁切机", "Hair-dryer thermal fuse cut-to-length machine", "Máy cắt tự động theo chiều dài cầu chì nhiệt máy sấy tóc"),
    ("dryer", None, "电吹风折叠手柄咔嗒环定量自动涂油机", "Hair-dryer folding-handle click ring metered greasing machine", "Máy tra mỡ định lượng tự động vòng khóa tay cầm gập máy sấy tóc"),
    ("shaver", "shaver-contact-base-assembly.jpg", "剃须刀接点基台A自动组立设备", "Shaver contact base (A) assembly machine", "Máy lắp ráp tự động đế tiếp điểm (A) máy cạo râu"),
    ("shaver", "shaver-spring-assembly.jpg", "剃须刀刃架操作口弹簧自动组立设备", "Shaver blade-holder spring assembly machine", "Máy lắp ráp tự động lò xo giá lưỡi máy cạo râu"),
    ("shaver", None, "旋转刀头剃须刀马达轴套切割与吹屑、正反转检测一体机", "Rotary shaver motor sleeve cutting, debris blowing and rotation test machine", "Máy tích hợp cắt ống lót trục motor, thổi phoi và kiểm tra chiều quay cho máy cạo râu đầu xoay"),
    ("shaver", None, "鼻毛器马达组件自动组装设备", "Nose-trimmer motor assembly machine", "Máy lắp ráp tự động cụm motor máy tỉa lông mũi"),
    ("shaver", "nose-trimmer-motor-sleeve-press.jpg", "鼻毛器马达轴套压接自动化设备", "Nose-trimmer motor shaft sleeve press-fit machine", "Máy ép tự động ống lót trục motor máy tỉa lông mũi"),
    ("shaver", None, "剃毛器肌身滚轮轴自动套入设备", "Body-shaver roller shaft insertion machine", "Máy lắp tự động trục con lăn máy cạo lông"),
    ("shaver", "clipper-screwing-waterproof-test.jpg", "理发器打螺丝、防水性能检测一体机", "Hair-clipper screw-driving and waterproof test machine", "Máy tích hợp bắt vít và kiểm tra chống nước tông đơ"),
    ("shaver", None, "剃须刀全自动打螺丝防水检测一体设备", "Shaver automatic screw-driving and waterproof test machine", "Máy tích hợp bắt vít tự động và kiểm tra chống nước máy cạo râu"),
    ("brush", "toothbrush-motor-shaft-press.jpg", "电动牙刷马达压轴自动化设备", "Electric toothbrush motor shaft press machine", "Máy ép trục motor bàn chải điện tự động"),
    ("brush", None, "电动牙刷头吸塑高周波焊接包装自动设备", "Toothbrush head blister high-frequency welding and packing machine", "Máy hàn cao tần và đóng gói vỉ nhựa đầu bàn chải điện"),
    ("brush", "toothbrush-assembly-test-line.jpg", "电动牙刷组装检测生产线", "Electric toothbrush assembly and test line", "Dây chuyền lắp ráp và kiểm tra bàn chải điện"),
    ("test", None, "剃须刀浮动刀头寿命试验机", "Shaver floating-head life tester", "Máy thử tuổi thọ đầu lưỡi nổi máy cạo râu"),
    ("test", None, "剃须刀刀刃推压寿命试验机", "Shaver blade push-pressure life tester", "Máy thử tuổi thọ lực ấn lưỡi máy cạo râu"),
    ("test", None, "剃须刀开关寿命测试机", "Shaver switch life tester", "Máy thử tuổi thọ công tắc máy cạo râu"),
    ("test", "shaver-water-immersion-life-test.jpg", "剃须刀温、冷水浸泡运转寿命试验设备", "Shaver hot and cold water immersion running life tester", "Thiết bị thử tuổi thọ vận hành khi ngâm nước nóng và lạnh cho máy cạo râu"),
    ("test", None, "往复式剃须刀刀头振幅测试设备", "Reciprocating shaver head amplitude tester", "Thiết bị đo biên độ đầu lưỡi máy cạo râu kiểu tịnh tiến"),
    ("test", None, "开关按压寿命试验机（定压力量）", "Switch press life tester (constant force)", "Máy thử tuổi thọ nhấn công tắc (lực không đổi)"),
    ("test", None, "本体气密性（防水性能）试验机", "Housing airtightness (waterproof) tester", "Máy thử độ kín khí (chống nước) của thân máy"),
    ("test", "airtight-waterproof-tester.jpg", "气密性（防水性能）检测设备", "Airtightness (waterproof) testing equipment", "Thiết bị kiểm tra độ kín khí (chống nước)"),
    ("elec", None, "二极管自动剪脚整形设备", "Diode lead cutting and forming machine", "Máy cắt và tạo hình chân điốt tự động"),
    ("elec", None, "电阻胶套套入整形自动设备", "Resistor sleeve insertion and forming machine", "Máy lồng ống bọc và tạo hình điện trở tự động"),
    ("elec", "pcb-auto-soldering.jpg", "电路板自动焊接设备", "PCB automatic soldering machine", "Máy hàn bo mạch tự động"),
    ("stamp", None, "圆形泵盖（∮48 和 ∮32mm）自动烫印生产设备", "Round pump cap (Ø48 / Ø32 mm) automatic hot-stamping machine", "Máy ép nhũ nóng tự động nắp bơm tròn (Ø48 / Ø32 mm)"),
    ("stamp", "mascara-cap-hot-stamping.jpg", "睫毛膏盖子异形镂空字体全自动烫印设备", "Mascara cap shaped-lettering automatic hot-stamping machine", "Máy ép nhũ nóng tự động chữ rỗng định hình trên nắp mascara"),
    ("stamp", "auto-grille-hot-stamping-10t.jpg", "10T 大型汽车进气格栅烫印设备", "10-tonne automotive grille hot-stamping press", "Máy ép nhũ nóng 10 tấn cho lưới tản nhiệt ô tô"),
    ("stamp", None, "激光刻印雕刻打标机", "Laser engraving and marking machine", "Máy khắc và đánh dấu bằng laser"),
    ("line", "smart-lock-laser-welding-line.jpg", "智能锁激光焊组装旋铆生产线", "Smart-lock laser welding, assembly and orbital riveting line", "Dây chuyền hàn laser, lắp ráp và tán xoay khóa thông minh"),
    ("line", "ptc-heater-assembly-test-line.jpg", "新能源汽车电池保护 PTC 电阻水发热包组装检测生产线", "EV battery-protection PTC water heater assembly and test line", "Dây chuyền lắp ráp và kiểm tra cụm sưởi nước PTC bảo vệ pin xe điện"),
]

# ── projects (anonymised) ──────────────────────────────────────────────────
PROJECTS = [
    {"imgs": ["eq/ptc-line-a.jpg", "eq/ptc-line-b.jpg", "eq/ptc-module.jpg"],
     "t": {"en": "EV battery PTC water heater: two-stage assembly and test line", "vi": "Cụm sưởi nước PTC cho pin xe điện: dây chuyền lắp ráp và kiểm tra hai giai đoạn", "zh": "新能源汽车电池 PTC 水发热包：两段式组装检测线"},
     "ind": {"en": "EV components", "vi": "Linh kiện xe điện", "zh": "新能源汽车零部件"},
     "d": {"en": ["Stage A presses PTC elements between electrode plates into finished heating cores.",
                  "Stage B covers housing sealing, high/low-voltage connector fitting, IGBT and PCBA installation, soldering, dispensing and AOI inspection, cover sealing, labelling, and hi-pot and resistance testing.",
                  "Every station scans the part, so each unit carries a production record."],
           "vi": ["Giai đoạn A ép phần tử PTC giữa các tấm điện cực thành lõi gia nhiệt.",
                  "Giai đoạn B gồm làm kín vỏ, lắp đầu nối cao/hạ áp, lắp IGBT và PCBA, hàn, tra keo và kiểm tra AOI, làm kín nắp, dán nhãn, kiểm tra cao áp và điện trở.",
                  "Mỗi trạm đều quét mã sản phẩm, nên từng sản phẩm có hồ sơ sản xuất riêng."],
           "zh": ["A 段将 PTC 元件与电极片压合成发热芯。",
                  "B 段包括壳体密封、高低压座安装、IGBT 与 PCBA 安装、焊接、点胶与 AOI 检测、盖板密封、贴标，以及耐压与电阻测试。",
                  "各工位扫码，每件产品都有生产记录。"]}},
    {"imgs": ["eq/laser-line-overview.jpg", "eq/laser-weld-cell.jpg", "eq/laser-line-operator.jpg"],
     "t": {"en": "Smart lock body: laser welding, assembly and orbital riveting line", "vi": "Thân khóa thông minh: dây chuyền hàn laser, lắp ráp và tán xoay", "zh": "智能锁锁体：激光焊接、组装与旋铆生产线"},
     "ind": {"en": "Locks & hardware", "vi": "Khóa & kim khí", "zh": "锁具与五金"},
     "d": {"en": ["Laser welding cells join the lock-body parts with fume extraction at each cell.",
                  "Assembly and orbital riveting stations are linked by a conveyor into one line.",
                  "Operators load parts at ergonomic stations; the line controls the welding and riveting."],
           "vi": ["Các trạm hàn laser liên kết chi tiết thân khóa, mỗi trạm có hệ thống hút khói.",
                  "Các trạm lắp ráp và tán xoay được nối bằng băng tải thành một dây chuyền.",
                  "Công nhân cấp phôi tại trạm thao tác; dây chuyền điều khiển quá trình hàn và tán."],
           "zh": ["激光焊接工位完成锁体零件焊接，各工位配烟尘净化。",
                  "组装与旋铆工位由输送线串成整线。",
                  "操作工在工位上料，焊接与旋铆由设备完成。"]}},
    {"imgs": ["eq/toothbrush-assembly-test-line.jpg", "eq/toothbrush-motor-shaft-press.jpg", "eq/robot-assembly-cell.jpg"],
     "t": {"en": "Electric toothbrush: assembly and test line", "vi": "Bàn chải điện: dây chuyền lắp ráp và kiểm tra", "zh": "电动牙刷：组装检测生产线"},
     "ind": {"en": "Personal care", "vi": "Chăm sóc cá nhân", "zh": "个护电器"},
     "d": {"en": ["Motor shaft press-fit, assembly and functional testing in one line.",
                  "Robot cells handle repetitive transfer and assembly steps.",
                  "Paired with blister welding and packing machines for brush heads."],
           "vi": ["Ép trục motor, lắp ráp và kiểm tra chức năng trên cùng một dây chuyền.",
                  "Robot đảm nhận các công đoạn chuyển và lắp ráp lặp lại.",
                  "Kết hợp với máy hàn và đóng gói vỉ cho đầu bàn chải."],
           "zh": ["马达压轴、组装与功能测试在一条线上完成。",
                  "机器人工作站承担重复的转运与组装工序。",
                  "可配套刷头吸塑焊接包装设备。"]}},
    {"imgs": ["eq/vision-hot-stamp-defect.jpg", "eq/vision-screwdriving.jpg", "eq/vision-glue-inspection.jpg"],
     "t": {"en": "CCD vision inspection across product lines", "vi": "Kiểm tra bằng camera CCD trên nhiều dòng sản phẩm", "zh": "CCD 视觉检测的多场景应用"},
     "ind": {"en": "Vision inspection", "vi": "Kiểm tra bằng camera", "zh": "视觉检测"},
     "d": {"en": ["Hot-stamping defect detection: wrinkles, cracks, gloss and whitening.",
                  "Vision-guided laser marking, assembly and screw-driving.",
                  "Glue inspection for missing, short or broken beads; sorting by colour and shape."],
           "vi": ["Phát hiện lỗi ép nhũ: nhăn, nứt, bóng và trắng mờ.",
                  "Khắc laser, lắp ráp và bắt vít định vị bằng camera.",
                  "Kiểm tra keo thiếu, ít hoặc đứt; phân loại theo màu và hình dạng."],
           "zh": ["烫金瑕疵检测：褶皱、裂痕、发亮、发白。",
                  "视觉定位激光打标、组装与锁螺丝。",
                  "点胶漏胶、少胶、缺口检测；按颜色与形状分选。"]}},
    {"imgs": ["site/workshop-2.jpg"],
     "t": {"en": "Garment production-line equipment, Vietnam", "vi": "Thiết bị dây chuyền may, Việt Nam", "zh": "服装生产线设备（越南）"},
     "ind": {"en": "Garment", "vi": "May mặc", "zh": "服装"},
     "d": {"en": ["Production-line equipment designed and pre-tested in Guangzhou for a garment factory in Vietnam.",
                  "Shipped, installed and commissioned at the customer's factory.",
                  "Project details are shared on request with the customer's agreement."],
           "vi": ["Thiết bị dây chuyền được thiết kế và chạy thử tại Quảng Châu cho một nhà máy may ở Việt Nam.",
                  "Đã vận chuyển, lắp đặt và chạy thử tại nhà máy khách hàng.",
                  "Thông tin chi tiết được cung cấp khi có yêu cầu và được khách hàng đồng ý."],
           "zh": ["为越南一家服装工厂设计并在广州完成预测试的生产线设备。",
                  "已发运并在客户工厂完成安装调试。",
                  "项目详情经客户同意后可应询提供。"]}},
]

ABOUT = {
    "h": {"en": "About Longteng Automation", "vi": "Về Longteng Automation", "zh": "关于龙腾自动化"},
    "p": {"en": ["Guangzhou Longteng Automation Equipment Co., Ltd. was founded in May 2019 in Panyu District, Guangzhou. The company registered its own trademark at the start and began as a design team; in September 2019 it opened its own production base in the Shibi industrial area and has designed and built its machines in-house since then.",
                 "We build fixtures, automatic assembly and test equipment, hot-stamping, pad-printing and silk-screen machines, appearance inspection systems and complete assembly lines for small appliances, cosmetics packaging and automotive parts, and more recently for medical, printing and packaging customers.",
                 "Longteng was recognised as a National High-Tech Enterprise in 2025 and holds nine granted patents."],
          "vi": ["Công ty TNHH Thiết bị Tự động hóa Longteng Quảng Châu được thành lập vào tháng 5/2019 tại quận Phiên Ngung (Panyu), Quảng Châu. Công ty đăng ký nhãn hiệu riêng ngay từ đầu và khởi đầu là một nhóm thiết kế; từ tháng 9/2019 công ty có xưởng sản xuất riêng tại khu công nghiệp Thạch Bích (Shibi) và tự thiết kế, chế tạo máy kể từ đó.",
                 "Chúng tôi chế tạo đồ gá, thiết bị lắp ráp và kiểm tra tự động, máy ép nhũ nóng, in tampon và in lụa, hệ thống kiểm tra ngoại quan và dây chuyền lắp ráp hoàn chỉnh cho điện gia dụng nhỏ, bao bì mỹ phẩm và linh kiện ô tô, và gần đây cho các ngành y tế, in ấn và bao bì.",
                 "Longteng được công nhận là Doanh nghiệp Công nghệ cao cấp quốc gia năm 2025 và sở hữu 9 bằng sáng chế đã được cấp."],
          "zh": ["广州龙腾自动化设备有限公司成立于 2019 年 5 月，位于广州市番禺区。公司成立之初即注册了自有品牌商标，最初以设计团队、外发生产的形式经营；2019 年 9 月在石壁街屏山工业区建立自有生产基地，此后自主设计研发、自主生产。",
                 "公司主营小家电、化妆品包材、汽车零部件等行业的工装夹具、自动组装检测设备，烫印、移印、丝印自动化设备，外观检测设备和电子制造组立生产线；近年来也开展了医疗、印刷、包装等行业的业务。",
                 "公司 2025 年获认定为国家高新技术企业，拥有授权专利 9 件。"]},
    "values": {"en": [("Industry experience", "Years of automation experience; every machine is built to the customer's product."),
                      ("Engineering strength", "Mechanical design, electrical engineering and production teams under one roof."),
                      ("Quality assurance", "Selected suppliers and a factory acceptance test for every machine before it ships."),
                      ("Careful installation", "Installation technicians with over ten years' experience test the machine on site and train your operators."),
                      ("After-sales service", "A named contact for any question during use, plus remote diagnosis.")],
               "vi": [("Kinh nghiệm ngành", "Nhiều năm kinh nghiệm tự động hóa; mỗi máy được chế tạo theo sản phẩm của khách hàng."),
                      ("Năng lực kỹ thuật", "Các nhóm thiết kế cơ khí, kỹ thuật điện và sản xuất làm việc tại cùng một nơi."),
                      ("Đảm bảo chất lượng", "Nhà cung cấp được chọn lọc; mỗi máy đều được nghiệm thu tại xưởng trước khi giao."),
                      ("Lắp đặt cẩn thận", "Kỹ thuật viên lắp đặt trên mười năm kinh nghiệm chạy thử tại chỗ và đào tạo công nhân vận hành."),
                      ("Dịch vụ sau bán hàng", "Có người phụ trách cho mọi thắc mắc trong quá trình sử dụng, cùng chẩn đoán từ xa.")],
               "zh": [("行业经验丰富", "多年自动化设备经验，每台设备按客户产品专属定制。"),
                      ("实力保障", "机械设计、电气工程与生产团队齐全。"),
                      ("质量保证", "严选供应商，每台设备出厂前都经过检验。"),
                      ("严谨的安装服务", "选派十年以上经验的安装师傅，现场测试并培训操作人员。"),
                      ("完善的售后服务", "使用中遇到问题随时联系，专人服务，并可远程诊断。")]},
}

CONTACT = {
    "h": {"en": "Request a quote", "vi": "Yêu cầu báo giá", "zh": "获取报价"},
    "sub": {"en": "Describe your product and process; attach drawings, photos or videos by email. We reply within one working day in English, Vietnamese or Chinese.",
            "vi": "Mô tả sản phẩm và quy trình; gửi kèm bản vẽ, ảnh hoặc video qua email. Chúng tôi phản hồi trong một ngày làm việc bằng tiếng Anh, tiếng Việt hoặc tiếng Trung.",
            "zh": "请描述您的产品与工序，并通过邮件发送图纸、照片或视频。我们会在一个工作日内用英文、越南文或中文回复。"},
    "fields": {"en": ["Company", "Factory location (province)", "Your name", "Email / Zalo / WhatsApp", "Product, target output per hour, current process…", "Prepare email"],
               "vi": ["Công ty", "Địa điểm nhà máy (tỉnh)", "Họ tên", "Email / Zalo / WhatsApp", "Sản phẩm, sản lượng mục tiêu mỗi giờ, quy trình hiện tại…", "Soạn email"],
               "zh": ["公司名称", "工厂所在省份", "联系人", "邮箱 / Zalo / WhatsApp", "产品、目标每小时产能、现有工艺……", "生成邮件"]},
    "labels": {"en": ["Email", "Phone", "Factory", "Languages"], "vi": ["Email", "Điện thoại", "Nhà máy", "Ngôn ngữ"], "zh": ["邮箱", "电话", "工厂地址", "沟通语言"]},
    "addr": {"en": "Annex 107, No. 7, 4th Street, Ping'er Industrial Zone, Shibi Street, Panyu District, Guangzhou, Guangdong, China",
             "vi": "Số 7 (phụ 107), Phố 4, Khu công nghiệp Ping'er, phường Thạch Bích (Shibi), quận Phiên Ngung (Panyu), Quảng Châu, Quảng Đông, Trung Quốc",
             "zh": "广州市番禺区石壁街道屏二工业区四街 7 号附 107 号"},
    "langs": {"en": "English · Tiếng Việt · 中文", "vi": "Tiếng Anh · Tiếng Việt · Tiếng Trung", "zh": "英文 · 越南文 · 中文"},
}

PAGE_TITLES = {
    "index": {"en": "Custom assembly & test lines", "vi": "Dây chuyền lắp ráp & kiểm tra theo yêu cầu", "zh": "定制装配与检测整线"},
    "solutions": {"en": "Solutions by industry", "vi": "Giải pháp theo ngành", "zh": "行业方案"},
    "equipment": {"en": "Equipment", "vi": "Thiết bị", "zh": "设备产品"},
    "projects": {"en": "Projects", "vi": "Dự án", "zh": "项目案例"},
    "about": {"en": "About us", "vi": "Giới thiệu", "zh": "关于我们"},
    "contact": {"en": "Contact & quote", "vi": "Liên hệ & báo giá", "zh": "联系我们"},
}
DESC = {"en": "Longteng Automation builds custom assembly, test, vision-inspection, laser-welding and hot-stamping equipment and complete lines for factories in Vietnam and worldwide.",
        "vi": "Longteng Automation chế tạo thiết bị lắp ráp, kiểm tra, kiểm tra bằng camera, hàn laser, ép nhũ nóng và dây chuyền hoàn chỉnh theo yêu cầu cho nhà máy tại Việt Nam.",
        "zh": "龙腾自动化为越南及海外工厂定制装配、检测、视觉检测、激光焊接与烫印设备及整线。"}

# ── v2 additions (premium redesign, 2026-10-25) ───────────────────────────
T["nav"] = {"en": ["Home", "Solutions", "Equipment", "Projects", "Innovation", "About", "Contact"],
            "vi": ["Trang chủ", "Giải pháp", "Thiết bị", "Dự án", "Công nghệ", "Giới thiệu", "Liên hệ"],
            "zh": ["首页", "行业方案", "设备产品", "项目案例", "技术与荣誉", "关于我们", "联系我们"]}
T["hero_kicker"] = {"en": "Non-standard automation · Engineered in Guangzhou · Delivered across Southeast Asia",
                    "vi": "Tự động hóa phi tiêu chuẩn · Thiết kế tại Quảng Châu · Triển khai khắp Đông Nam Á",
                    "zh": "非标自动化 · 广州研发制造 · 服务东南亚"}
T["hero_h1"] = {"en": "Precision automation that turns your product into a production line",
                "vi": "Tự động hóa chính xác — biến sản phẩm của bạn thành dây chuyền sản xuất",
                "zh": "以精密自动化，把您的产品变成一条高效产线"}
T["hero_p"] = {"en": "Assembly, testing, CCD vision inspection, laser welding and hot stamping — custom lines for appliance, electronics, EV-component, lock and packaging manufacturers. Designed and proven in our Guangzhou plant, installed and supported at your factory in Vietnam and across Southeast Asia.",
               "vi": "Lắp ráp, kiểm tra, kiểm tra bằng camera CCD, hàn laser và ép nhũ nóng — dây chuyền theo yêu cầu cho nhà sản xuất điện gia dụng, điện tử, linh kiện xe điện, khóa và bao bì. Thiết kế và chạy thử tại nhà máy Quảng Châu, lắp đặt và hỗ trợ tại nhà máy của bạn ở Việt Nam và Đông Nam Á.",
               "zh": "装配、检测、CCD 视觉检测、激光焊接与烫印——为小家电、电子、新能源汽车零部件、锁具与包装制造商定制整线。在广州工厂完成设计与验证，到您在越南及东南亚的工厂安装调试并长期服务。"}
T["hero_btn2"] = {"en": "Explore our equipment", "vi": "Khám phá thiết bị", "zh": "浏览设备"}
T["cta"] = {"en": "Talk to an engineer", "vi": "Trao đổi với kỹ sư", "zh": "联系工程师"}
T["quote"] = {"en": "Request a quote", "vi": "Yêu cầu báo giá", "zh": "获取报价"}

CAPS_H = {"en": "Core technologies", "vi": "Công nghệ cốt lõi", "zh": "核心技术"}
CAPS_SUB = {"en": "Four engineering capabilities, combined into machines and complete lines for your product.",
            "vi": "Bốn năng lực kỹ thuật, kết hợp thành máy và dây chuyền hoàn chỉnh cho sản phẩm của bạn.",
            "zh": "四项工程能力，组合成为您的产品量身定制的单机与整线。"}
CAPS = [
    ("assembly", {"en": "Precision assembly", "vi": "Lắp ráp chính xác", "zh": "精密装配"},
     {"en": "Riveting, press-fit, screw-driving, gluing and robot-cell assembly for small parts and sub-assemblies.",
      "vi": "Tán đinh, ép, bắt vít, tra keo và lắp ráp bằng robot cho chi tiết nhỏ và cụm lắp.",
      "zh": "铆接、压装、锁螺丝、点胶与机器人工作站，覆盖小零件与组件装配。"}),
    ("vision", {"en": "CCD vision inspection", "vi": "Kiểm tra bằng camera CCD", "zh": "CCD 视觉检测"},
     {"en": "Appearance defects, positioning, guided assembly, glue-bead inspection and multi-material sorting.",
      "vi": "Lỗi ngoại quan, định vị, lắp ráp theo camera, kiểm tra đường keo và phân loại vật liệu.",
      "zh": "外观瑕疵、定位、视觉引导组装、点胶检测与多物料分选。"}),
    ("laser", {"en": "Laser & surface processing", "vi": "Gia công laser & bề mặt", "zh": "激光与表面工艺"},
     {"en": "Laser welding and marking, hot stamping, pad printing and silk-screen automation.",
      "vi": "Hàn và khắc laser, ép nhũ nóng, in tampon và in lụa tự động.",
      "zh": "激光焊接与打标、烫印、移印与丝印自动化。"}),
    ("test", {"en": "Testing & traceability", "vi": "Kiểm tra & truy xuất", "zh": "检测与追溯"},
     {"en": "Airtight, waterproof, life, hi-pot and functional testing, with part scanning at every station.",
      "vi": "Kiểm tra kín khí, chống nước, tuổi thọ, cao áp và chức năng, quét mã tại mỗi trạm.",
      "zh": "气密、防水、寿命、耐压与功能测试，各工位扫码追溯。"}),
]

CREDS_H = {"en": "Recognition & certification", "vi": "Chứng nhận & ghi nhận", "zh": "资质与荣誉"}
CREDS = [
    ({"en": "National High-Tech Enterprise", "vi": "Doanh nghiệp Công nghệ cao cấp quốc gia", "zh": "国家高新技术企业"},
     {"en": "Certificate GR202544005832 · issued 19 Dec 2025", "vi": "Giấy chứng nhận GR202544005832 · cấp ngày 19/12/2025", "zh": "证书编号 GR202544005832 · 2025 年 12 月 19 日发证"}),
    ({"en": "Innovative SME of Guangdong Province", "vi": "Doanh nghiệp vừa và nhỏ đổi mới sáng tạo tỉnh Quảng Đông", "zh": "广东省创新型中小企业"},
     {"en": "Recognised 2025", "vi": "Công nhận năm 2025", "zh": "2025 年认定"}),
    ({"en": "Technology-based SME", "vi": "Doanh nghiệp vừa và nhỏ dựa trên công nghệ", "zh": "科技型中小企业"},
     {"en": "Registered 2023 · 2024 · 2025", "vi": "Đăng ký các năm 2023 · 2024 · 2025", "zh": "2023、2024、2025 年连续入库"}),
    ({"en": "9 granted patents", "vi": "9 bằng sáng chế đã được cấp", "zh": "9 件授权专利"},
     {"en": "8 utility models and 1 invention; 4 invention applications under examination", "vi": "8 giải pháp hữu ích và 1 sáng chế; 4 đơn sáng chế đang thẩm định", "zh": "实用新型 8 件、发明 1 件；另有 4 件发明专利在实审"}),
    ({"en": "Registered trademark «LT»", "vi": "Nhãn hiệu đã đăng ký «LT»", "zh": "注册商标「LT」"},
     {"en": "Class 7 (machinery) · Reg. No. 55741827", "vi": "Nhóm 7 (máy móc) · Số đăng ký 55741827", "zh": "第 7 类机械设备 · 注册号 55741827"}),
]

PATENTS_H = {"en": "Patent portfolio", "vi": "Danh mục sáng chế", "zh": "专利一览"}
PAT_COLS = {"en": ["Publication No.", "Title", "Type", "Status"], "vi": ["Số công bố", "Tên", "Loại", "Tình trạng"], "zh": ["公告号", "名称", "类型", "状态"]}
PAT_TYPE = {"inv": {"en": "Invention", "vi": "Sáng chế", "zh": "发明"}, "um": {"en": "Utility model", "vi": "Giải pháp hữu ích", "zh": "实用新型"}}
PAT_STATUS = {"g": {"en": "Granted", "vi": "Đã cấp", "zh": "已授权"}, "e": {"en": "Under examination", "vi": "Đang thẩm định", "zh": "实质审查中"}}
PATENTS = [
    ("CN111267132B", "inv", "g", {"en": "Clamping mechanism for industrial robots", "vi": "Cơ cấu kẹp cho robot công nghiệp", "zh": "一种用于工业机器人的夹持机构"}),
    ("CN222035448U", "um", "g", {"en": "PTC heater wrapping equipment", "vi": "Thiết bị bọc keo bộ gia nhiệt PTC", "zh": "PTC 加热器包胶设备"}),
    ("CN221910615U", "um", "g", {"en": "Inner and outer barrel fitting device for pen-type shavers", "vi": "Thiết bị lắp ống trong và ngoài cho máy cạo râu dạng bút", "zh": "笔式剃须刀内外筒安装装置"}),
    ("CN221791677U", "um", "g", {"en": "Aluminium tube threading device", "vi": "Thiết bị luồn ống nhôm", "zh": "铝管穿装装置"}),
    ("CN221714756U", "um", "g", {"en": "Automatic glue-dispensing equipment for thermostats", "vi": "Thiết bị tra keo tự động cho bộ điều nhiệt", "zh": "温控器自动点胶设备"}),
    ("CN221571564U", "um", "g", {"en": "Hair-dryer performance testing device", "vi": "Thiết bị kiểm tra hiệu năng máy sấy tóc", "zh": "电吹风性能检测装置"}),
    ("CN221565210U", "um", "g", {"en": "Film-winding device for tube-threading machines", "vi": "Cơ cấu cuộn màng cho máy luồn ống", "zh": "穿管机卷膜装置"}),
    ("CN221423656U", "um", "g", {"en": "PTC heater component shaping equipment", "vi": "Thiết bị tạo hình cụm sưởi PTC", "zh": "PTC 暖风机组件整形设备"}),
    ("CN218311948U", "um", "g", {"en": "Automatic forming machine for diode rectifier bridges", "vi": "Máy tạo hình tự động cầu chỉnh lưu điốt", "zh": "二极管整流桥自动成型机"}),
    ("CN118768729A", "inv", "e", {"en": "Laser welding equipment for lock bodies", "vi": "Thiết bị hàn laser cho thân khóa", "zh": "一种用于锁体焊接的激光焊接设备"}),
    ("CN118269023A", "inv", "e", {"en": "Forming fixture for PTC heating-element production lines", "vi": "Đồ gá tạo hình cho dây chuyền sản xuất phần tử gia nhiệt PTC", "zh": "一种 PTC 加热件生产流水线成型治具"}),
    ("CN117798656A", "inv", "e", {"en": "Automatic assembly equipment for USB boxes", "vi": "Thiết bị lắp ráp tự động hộp USB", "zh": "一种 USB 盒子自动组装设备"}),
    ("CN117719148A", "inv", "e", {"en": "Nozzle bending equipment for oral irrigators", "vi": "Thiết bị uốn vòi máy tăm nước", "zh": "一种冲牙器喷嘴弯曲设备"}),
]

SEA_H = {"en": "Built for Southeast Asia", "vi": "Dành cho Đông Nam Á", "zh": "面向东南亚"}
SEA_P = {"en": "Our engineers fly out from Guangzhou to install, commission and train on site. Factory acceptance tests can be witnessed in person or by live video, and every line ships with remote diagnostics and a spare-parts kit.",
         "vi": "Kỹ sư của chúng tôi bay từ Quảng Châu đến lắp đặt, chạy thử và đào tạo tại chỗ. Nghiệm thu tại xưởng có thể chứng kiến trực tiếp hoặc qua video trực tuyến; mỗi dây chuyền đều có chẩn đoán từ xa và bộ phụ tùng.",
         "zh": "工程师从广州出发，到现场安装调试与培训。出厂验收可到场或通过实时视频见证；每条产线都配远程诊断与备件包。"}
SEA_POINTS = {"en": ["About 2 hours' flight to Hanoi", "Live-video factory acceptance tests", "English, Vietnamese and Chinese support", "Remote diagnosis and spare-parts kits"],
              "vi": ["Khoảng 2 giờ bay đến Hà Nội", "Nghiệm thu tại xưởng qua video trực tuyến", "Hỗ trợ tiếng Anh, tiếng Việt và tiếng Trung", "Chẩn đoán từ xa và bộ phụ tùng"],
              "zh": ["至河内航程约 2 小时", "出厂验收可视频见证", "英文、越南文、中文支持", "远程诊断与备件包"]}
CITIES = [("Guangzhou", "Quảng Châu", "广州", 113.26, 23.13, ""), ("Hanoi", "Hà Nội", "河内", 105.85, 21.03, "≈2h"),
          ("Ho Chi Minh City", "TP. Hồ Chí Minh", "胡志明市", 106.70, 10.78, "≈3h"), ("Bangkok", "Bangkok", "曼谷", 100.50, 13.76, "≈3h"),
          ("Kuala Lumpur", "Kuala Lumpur", "吉隆坡", 101.69, 3.14, "≈4h"), ("Jakarta", "Jakarta", "雅加达", 106.85, -6.21, "≈5h"),
          ("Manila", "Manila", "马尼拉", 120.98, 14.60, "≈2h")]
SEA_NOTE = {"en": "Approximate direct flight times from Guangzhou.", "vi": "Thời gian bay thẳng ước tính từ Quảng Châu.", "zh": "自广州直飞的大致航程。"}

TIMELINE_H = {"en": "Milestones", "vi": "Các mốc phát triển", "zh": "发展历程"}
TIMELINE = [
    ("2019.05", {"en": "Founded in Guangzhou; own trademark registered", "vi": "Thành lập tại Quảng Châu; đăng ký nhãn hiệu riêng", "zh": "在广州成立，注册自有商标"}),
    ("2019.09", {"en": "Own production base opened in Panyu; in-house design and manufacturing", "vi": "Mở xưởng sản xuất riêng tại Phiên Ngung; tự thiết kế và chế tạo", "zh": "番禺自有生产基地投用，自主设计与制造"}),
    ("2023", {"en": "First utility-model patent granted; registered as a Technology-based SME", "vi": "Được cấp bằng giải pháp hữu ích đầu tiên; đăng ký doanh nghiệp vừa và nhỏ dựa trên công nghệ", "zh": "首件实用新型专利授权；入库科技型中小企业"}),
    ("2024", {"en": "Seven more utility-model patents granted", "vi": "Được cấp thêm 7 bằng giải pháp hữu ích", "zh": "再获 7 件实用新型专利授权"}),
    ("2025", {"en": "Invention patent for an industrial-robot clamping mechanism acquired; Innovative SME of Guangdong; National High-Tech Enterprise", "vi": "Nhận chuyển nhượng sáng chế cơ cấu kẹp robot công nghiệp; doanh nghiệp đổi mới sáng tạo tỉnh Quảng Đông; Doanh nghiệp Công nghệ cao cấp quốc gia", "zh": "受让工业机器人夹持机构发明专利；广东省创新型中小企业；国家高新技术企业"}),
    ("2026", {"en": "Trilingual export website launched for Southeast Asian customers", "vi": "Ra mắt website ba ngôn ngữ cho khách hàng Đông Nam Á", "zh": "上线面向东南亚客户的三语外贸网站"}),
]
INNOV_SUB = {"en": "Independent engineering, protected by patents and recognised by national and provincial programmes.",
             "vi": "Năng lực kỹ thuật độc lập, được bảo hộ bằng sáng chế và được các chương trình quốc gia, cấp tỉnh công nhận.",
             "zh": "自主研发能力，由专利保护，并获国家与省级认定。"}
PAGE_TITLES["innovation"] = {"en": "Innovation & recognition", "vi": "Công nghệ & chứng nhận", "zh": "技术与荣誉"}

# ── v3 additions (company photos, videos and certificates received 2026-10-25) ──
import json as _json, pathlib as _pl
VIDEOS = {v["code"]: v for v in _json.loads((_pl.Path(__file__).with_name("media.json")).read_text(encoding="utf-8"))}


def clip_len(code):
    d = VIDEOS[code]["duration_s"]
    return round(d) if d <= 34 else 30


FILTERS = [
    ("dryer", {"en": "Hair-dryer components", "vi": "Linh kiện máy sấy tóc", "zh": "电吹风零部件"}),
    ("care", {"en": "Personal & oral care", "vi": "Chăm sóc cá nhân & răng miệng", "zh": "个护与口腔护理"}),
    ("pack", {"en": "Cosmetic packaging & printing", "vi": "Bao bì mỹ phẩm & in ấn", "zh": "化妆品包材与印刷"}),
    ("auto", {"en": "EV & automotive", "vi": "Xe điện & ô tô", "zh": "新能源与汽车"}),
    ("lock", {"en": "Smart locks & hardware", "vi": "Khóa thông minh & kim khí", "zh": "智能锁与五金"}),
    ("elec", {"en": "Electronics & appliances", "vi": "Điện tử & đồ gia dụng", "zh": "电子电器"}),
    ("test", {"en": "Testing & life tests", "vi": "Kiểm tra & thử tuổi thọ", "zh": "检测与寿命试验"}),
]
_OLD2NEW = {"dryer": "dryer", "shaver": "care", "brush": "care", "test": "test", "elec": "elec", "stamp": "pack"}
_SPECIAL = {31: "auto", 33: "lock", 34: "auto"}
MACHINES = []
for _i, _e in enumerate(EQ):
    _v = next((c for c, v in VIDEOS.items() if v["catalogue_index"] == _i), None)
    MACHINES.append({"cat": _SPECIAL.get(_i, _OLD2NEW.get(_e[0])), "img": _e[1], "vid": _v, "zh": _e[2], "en": _e[3], "vi": _e[4]})
for _c, _v in VIDEOS.items():
    if _v["catalogue_index"] is None and _v["site_filter"] not in ("company", "media"):
        MACHINES.append({"cat": _v["site_filter"], "img": None, "vid": _c, **_v["title"]})

HOME_VIDEOS = ["D01", "C01", "A01", "E03", "B01", "C02"]
INDUSTRY_VIDEO = {"appliances": "A01", "vision": "F01", "locks": "E03", "ev": "D01", "packaging": "C02"}

VSTR = {
    "vid_k": {"en": "Machines in action", "vi": "Máy móc đang vận hành", "zh": "设备实拍"},
    "vid_h": {"en": "Real footage from our plant and our customers' factories",
              "vi": "Video thực tế từ nhà máy của chúng tôi và nhà máy khách hàng",
              "zh": "来自龙腾工厂与客户现场的真实视频"},
    "watch_all": {"en": "Watch all videos", "vi": "Xem tất cả video", "zh": "观看全部视频"},
    "with_video": {"en": "With video", "vi": "Có video", "zh": "有视频"},
    "play": {"en": "Play video", "vi": "Phát video", "zh": "播放视频"},
    "close": {"en": "Close", "vi": "Đóng", "zh": "关闭"},
    "eq_sub": {"en": "{n} machine types designed and built, grouped by application — {v} of them on video. Every machine is customised to your product.",
               "vi": "{n} loại máy đã thiết kế và chế tạo, phân theo ứng dụng — {v} loại có video. Mỗi máy đều được tùy biến theo sản phẩm của bạn.",
               "zh": "已设计制造的 {n} 类设备，按应用分组，其中 {v} 类有实拍视频；每台设备都按您的产品定制。"},
    "certwall_k": {"en": "Certificates", "vi": "Giấy chứng nhận", "zh": "证书"},
    "certwall_h": {"en": "Certificates and patent grants", "vi": "Giấy chứng nhận và bằng sáng chế", "zh": "资质证书与专利证书"},
    "certwall_note": {"en": "Click a certificate to enlarge it. Originals are available for audit on request.",
                      "vi": "Nhấn vào giấy chứng nhận để phóng to. Bản gốc được cung cấp khi đánh giá nhà cung cấp.",
                      "zh": "点击证书可放大查看；供应商审核时可提供原件。"},
    "tour_k": {"en": "Factory tour", "vi": "Tham quan nhà máy", "zh": "工厂实拍"},
    "tour_h": {"en": "Walk through our R&D and assembly workshop", "vi": "Tham quan xưởng R&D và lắp ráp", "zh": "走进研发中心与装配车间"},
    "tour_p": {"en": "Every machine is designed, assembled and tested here before it ships — and you are welcome to visit, or to join the factory acceptance test by live video.",
               "vi": "Mỗi máy đều được thiết kế, lắp ráp và chạy thử tại đây trước khi giao — quý khách có thể đến thăm hoặc tham gia nghiệm thu qua video trực tuyến.",
               "zh": "每台设备都在这里完成设计、装配与测试后才发货——欢迎到厂参观，或通过实时视频参加出厂验收。"},
}

TRUST = [
    {"en": "Featured on CCTV", "vi": "Lên sóng CCTV", "zh": "央视专访"},
    {"en": "National High-Tech Enterprise", "vi": "Doanh nghiệp Công nghệ cao cấp quốc gia", "zh": "国家高新技术企业"},
    {"en": "ISO 9001:2015 certified", "vi": "Chứng nhận ISO 9001:2015", "zh": "ISO 9001:2015 认证"},
    {"en": "Innovative SME of Guangdong", "vi": "Doanh nghiệp đổi mới sáng tạo Quảng Đông", "zh": "广东省创新型中小企业"},
    {"en": "9 granted patents", "vi": "9 bằng sáng chế", "zh": "9 件授权专利"},
]

CREDS.insert(1, ({"en": "ISO 9001:2015 quality management", "vi": "Hệ thống quản lý chất lượng ISO 9001:2015", "zh": "ISO 9001:2015 质量管理体系"},
                 {"en": "Certificate ZGTC22Q01563R0 · valid to 31 Mar 2028", "vi": "Chứng chỉ ZGTC22Q01563R0 · hiệu lực đến 31/03/2028", "zh": "证书号 ZGTC22Q01563R0 · 有效期至 2028 年 3 月 31 日"}))

CERTWALL = [
    ("cert/hnte.jpg", {"en": "National High-Tech Enterprise", "vi": "Doanh nghiệp Công nghệ cao", "zh": "国家高新技术企业证书"}),
    ("cert/iso9001-en.jpg", {"en": "ISO 9001:2015 certificate", "vi": "Chứng chỉ ISO 9001:2015", "zh": "ISO 9001:2015 证书"}),
    ("cert/trademark.jpg", {"en": "Trademark registration «LT»", "vi": "Đăng ký nhãn hiệu «LT»", "zh": "商标注册证"}),
    ("cert/pat-CN221571564U.jpg", {"en": "Patent CN221571564U", "vi": "Bằng CN221571564U", "zh": "专利 CN221571564U"}),
    ("cert/pat-CN221714756U.jpg", {"en": "Patent CN221714756U", "vi": "Bằng CN221714756U", "zh": "专利 CN221714756U"}),
    ("cert/pat-CN221423656U.jpg", {"en": "Patent CN221423656U", "vi": "Bằng CN221423656U", "zh": "专利 CN221423656U"}),
    ("cert/pat-CN221910615U.jpg", {"en": "Patent CN221910615U", "vi": "Bằng CN221910615U", "zh": "专利 CN221910615U"}),
    ("cert/pat-CN221791677U.jpg", {"en": "Patent CN221791677U", "vi": "Bằng CN221791677U", "zh": "专利 CN221791677U"}),
    ("cert/pat-CN221565210U.jpg", {"en": "Patent CN221565210U", "vi": "Bằng CN221565210U", "zh": "专利 CN221565210U"}),
    ("cert/pat-CN218311948U.jpg", {"en": "Patent CN218311948U", "vi": "Bằng CN218311948U", "zh": "专利 CN218311948U"}),
]

MEDIA = {
    "k": {"en": "In the media", "vi": "Truyền thông", "zh": "媒体报道"},
    "h": {"en": "Featured on CCTV", "vi": "Được giới thiệu trên CCTV", "zh": "央视专访"},
    "p": {"en": "China Central Television (CCTV) interviewed our general manager, Cao Chengpei, for its series “Rising National Brands” — on how Longteng helps manufacturers upgrade their production with automation.",
          "vi": "Đài Truyền hình Trung ương Trung Quốc (CCTV) đã phỏng vấn Tổng giám đốc Tào Thành Bồi (Cao Chengpei) trong chuyên mục “Thương hiệu dân tộc vươn lên”, về cách Longteng giúp các nhà sản xuất nâng cấp sản xuất bằng tự động hóa.",
          "zh": "中央电视台《崛起的民族品牌》专题节目专访总经理曹城培，讲述龙腾如何以自动化助力制造企业转型升级。"},
    "points": {"en": ["Full-lifecycle service: diagnosis, design, manufacturing, installation & commissioning, and data support after start-up.",
                      "Modular quick-change design — one product changeover cut from 4 hours to 20 minutes.",
                      "A process knowledge base of 2,000+ entries, built from the parameters and lessons of past projects."],
               "vi": ["Dịch vụ trọn vòng đời: khảo sát nhu cầu, thiết kế, chế tạo, lắp đặt – chạy thử và hỗ trợ dữ liệu sau vận hành.",
                      "Thiết kế mô-đun thay nhanh — thời gian chuyển đổi một sản phẩm giảm từ 4 giờ xuống 20 phút.",
                      "Kho tri thức quy trình hơn 2.000 mục, tích lũy từ thông số và kinh nghiệm của các dự án đã thực hiện."],
               "zh": ["全生命周期服务：需求诊断、方案设计、设备制造、安装调试与数据运维。",
                      "模块化快速换线设计——一次换型从 4 小时缩短到 20 分钟。",
                      "积累 2000 余条数据的制造知识库，沉淀历次项目的工艺参数与经验。"]},
    "note": {"en": "Programme: “Rising National Brands” (崛起的民族品牌), CCTV.", "vi": "Chương trình: “Thương hiệu dân tộc vươn lên” (崛起的民族品牌), CCTV.", "zh": "节目：中央电视台《崛起的民族品牌》。"},
}

EXPORT = {
    "k": {"en": "Export-ready", "vi": "Sẵn sàng xuất khẩu", "zh": "出口就绪"},
    "h": {"en": "Built for factories in Southeast Asia and Europe", "vi": "Dành cho nhà máy ở Đông Nam Á và châu Âu", "zh": "面向东南亚与欧洲工厂"},
    "p": {"en": "Our customers include plants of a Japanese home-appliance group in China and Thailand and of a European electrical-equipment group, and production equipment has been delivered to Vietnam. Every export project follows the same routine.",
          "vi": "Khách hàng của chúng tôi gồm các nhà máy của một tập đoàn điện gia dụng Nhật Bản tại Trung Quốc và Thái Lan, và của một tập đoàn thiết bị điện châu Âu; thiết bị sản xuất đã được giao tới Việt Nam. Mọi dự án xuất khẩu đều theo cùng một quy trình.",
          "zh": "客户包括某日系家电集团在中国与泰国的工厂、某欧洲电气集团的工厂，生产设备已交付越南。每个出口项目都遵循同一套流程。"},
    "items": [
        ("badge", {"en": "ISO 9001:2015 quality system", "vi": "Hệ thống chất lượng ISO 9001:2015", "zh": "ISO 9001:2015 质量体系"},
         {"en": "Design, build and inspection run under a certified quality management system.", "vi": "Thiết kế, chế tạo và kiểm tra vận hành theo hệ thống quản lý chất lượng được chứng nhận.", "zh": "设计、制造与检验在认证的质量管理体系下运行。"}),
        ("video", {"en": "FAT on site or by live video", "vi": "Nghiệm thu FAT trực tiếp hoặc qua video", "zh": "出厂验收可到场或视频见证"},
         {"en": "Run your own parts on the machine in Guangzhou before it ships.", "vi": "Chạy thử bằng chính chi tiết của bạn tại Quảng Châu trước khi giao.", "zh": "发货前在广州用您的零件试机。"}),
        ("chat", {"en": "English & Vietnamese support", "vi": "Hỗ trợ tiếng Anh & tiếng Việt", "zh": "英文与越南文支持"},
         {"en": "Quotations, manuals and operator screens in English; Vietnamese on request.", "vi": "Báo giá, hướng dẫn và màn hình vận hành bằng tiếng Anh; tiếng Việt theo yêu cầu.", "zh": "报价、说明书与操作界面提供英文，越南文可按需提供。"}),
        ("plane", {"en": "Shipping & export documents", "vi": "Vận chuyển & chứng từ xuất khẩu", "zh": "运输与出口单证"},
         {"en": "CIF to Hai Phong, Ho Chi Minh City, Bangkok or European ports, with certificate of origin.", "vi": "Giao CIF đến Hải Phòng, TP. HCM, Bangkok hoặc cảng châu Âu, kèm C/O.", "zh": "可按 CIF 发运至海防、胡志明市、曼谷或欧洲港口，提供原产地证。"}),
    ],
}

T["stats"] = {"en": [("2019", "Founded in Guangzhou"), ("National", "High-Tech Enterprise (2025)"), ("ISO 9001", "Certified quality system"), ("9", "Granted patents"), ("50+", "Machine types designed & built")],
              "vi": [("2019", "Thành lập tại Quảng Châu"), ("Quốc gia", "Doanh nghiệp công nghệ cao (2025)"), ("ISO 9001", "Hệ thống chất lượng được chứng nhận"), ("9", "Bằng sáng chế được cấp"), ("50+", "Loại máy đã thiết kế & chế tạo")],
              "zh": [("2019", "成立于广州"), ("国家级", "高新技术企业（2025）"), ("ISO 9001", "质量管理体系认证"), ("9 件", "授权专利"), ("50+", "已设计制造的设备类型")]}
T["hero_kicker"] = {"en": "Non-standard automation · Engineered in Guangzhou · For factories in Southeast Asia and Europe",
                    "vi": "Tự động hóa phi tiêu chuẩn · Thiết kế tại Quảng Châu · Cho nhà máy ở Đông Nam Á và châu Âu",
                    "zh": "非标自动化 · 广州研发制造 · 服务东南亚与欧洲工厂"}
T["hero_p"] = {"en": "Assembly, testing, CCD vision inspection, laser welding and hot stamping — custom machines and lines for appliance, personal-care, cosmetics-packaging, EV-component, lock and electronics manufacturers. Designed and proven in our Guangzhou plant, installed and supported at your factory in Southeast Asia and Europe.",
               "vi": "Lắp ráp, kiểm tra, kiểm tra bằng camera CCD, hàn laser và ép nhũ nóng — máy và dây chuyền theo yêu cầu cho nhà sản xuất điện gia dụng, sản phẩm chăm sóc cá nhân, bao bì mỹ phẩm, linh kiện xe điện, khóa và điện tử. Thiết kế và chạy thử tại nhà máy Quảng Châu, lắp đặt và hỗ trợ tại nhà máy của bạn ở Đông Nam Á và châu Âu.",
               "zh": "装配、检测、CCD 视觉检测、激光焊接与烫印——为小家电、个护、化妆品包材、新能源汽车零部件、锁具与电子制造商定制单机与整线。在广州工厂完成设计与验证，到您在东南亚与欧洲的工厂安装调试并长期服务。"}
DESC = {"en": "Longteng Automation (Guangzhou) builds custom assembly, test, CCD vision-inspection, laser-welding and hot-stamping machines and complete lines for factories in Vietnam, Southeast Asia and Europe. ISO 9001:2015, National High-Tech Enterprise, featured on CCTV.",
        "vi": "Longteng Automation (Quảng Châu) chế tạo máy lắp ráp, kiểm tra, kiểm tra bằng camera CCD, hàn laser, ép nhũ nóng và dây chuyền hoàn chỉnh theo yêu cầu cho nhà máy tại Việt Nam, Đông Nam Á và châu Âu. ISO 9001:2015, Doanh nghiệp Công nghệ cao, được giới thiệu trên CCTV.",
        "zh": "龙腾自动化（广州）为越南、东南亚与欧洲工厂定制装配、检测、CCD 视觉检测、激光焊接与烫印设备及整线。ISO 9001:2015 认证，国家高新技术企业，央视专访企业。"}
TIMELINE[4] = ("2025", {"en": "ISO 9001:2015 certified; invention patent for an industrial-robot clamping mechanism acquired; Innovative SME of Guangdong; National High-Tech Enterprise",
                        "vi": "Đạt chứng nhận ISO 9001:2015; nhận chuyển nhượng sáng chế cơ cấu kẹp robot công nghiệp; doanh nghiệp đổi mới sáng tạo Quảng Đông; Doanh nghiệp Công nghệ cao cấp quốc gia",
                        "zh": "通过 ISO 9001:2015 认证；受让工业机器人夹持机构发明专利；广东省创新型中小企业；国家高新技术企业"})
TIMELINE[5] = ("2026", {"en": "Featured on CCTV; trilingual export website launched for customers in Southeast Asia and Europe",
                        "vi": "Được giới thiệu trên CCTV; ra mắt website ba ngôn ngữ cho khách hàng Đông Nam Á và châu Âu",
                        "zh": "接受央视专访；上线面向东南亚与欧洲客户的三语外贸网站"})
ABOUT["p"] = {
    "en": ["Guangzhou Longteng Automation Equipment Co., Ltd. was founded in May 2019 in Panyu District, Guangzhou. The company registered its own trademark at the start and began as a design team; in September 2019 it opened its own production base in the Shibi industrial area and has designed and built its machines in-house since then.",
           "We build fixtures, automatic assembly and test equipment, hot-stamping, pad-printing and screen-printing machines, CCD appearance-inspection systems and complete assembly lines for small appliances, electronics, cosmetics, food, medical devices, garments and automotive parts.",
           "Our general manager, Cao Chengpei, brings three decades of hands-on experience in precision manufacturing. Longteng is a National High-Tech Enterprise, runs an ISO 9001:2015 certified quality system and holds nine granted patents."],
    "vi": ["Công ty TNHH Thiết bị Tự động hóa Longteng Quảng Châu được thành lập vào tháng 5/2019 tại quận Phiên Ngung (Panyu), Quảng Châu. Công ty đăng ký nhãn hiệu riêng ngay từ đầu và khởi đầu là một nhóm thiết kế; từ tháng 9/2019 công ty có xưởng sản xuất riêng tại khu công nghiệp Thạch Bích (Shibi) và tự thiết kế, chế tạo máy kể từ đó.",
           "Chúng tôi chế tạo đồ gá, thiết bị lắp ráp và kiểm tra tự động, máy ép nhũ nóng, in tampon và in lụa, hệ thống kiểm tra ngoại quan bằng camera CCD và dây chuyền lắp ráp hoàn chỉnh cho điện gia dụng nhỏ, điện tử, mỹ phẩm, thực phẩm, thiết bị y tế, may mặc và linh kiện ô tô.",
           "Tổng giám đốc Tào Thành Bồi (Cao Chengpei) có ba mươi năm kinh nghiệm thực tế trong sản xuất chính xác. Longteng là Doanh nghiệp Công nghệ cao cấp quốc gia, vận hành hệ thống chất lượng đạt chứng nhận ISO 9001:2015 và sở hữu 9 bằng sáng chế đã được cấp."],
    "zh": ["广州龙腾自动化设备有限公司成立于 2019 年 5 月，位于广州市番禺区。公司成立之初即注册了自有品牌商标，最初以设计团队、外发生产的形式经营；2019 年 9 月在石壁街屏山工业区建立自有生产基地，此后自主设计研发、自主生产。",
           "公司主营小家电、电子、化妆品、食品、医疗器械、服装、汽车零部件等制造行业的工装夹具、自动组装检测设备及生产线，烫印、移印、丝印自动化设备，CCD 外观检测设备与电子制造自动组立生产线。",
           "总经理曹城培在精密制造领域深耕三十年。公司是国家高新技术企业，通过 ISO 9001:2015 质量管理体系认证，拥有授权专利 9 件。"]}
PROJECTS[0]["vid"] = "D01"
PROJECTS[0]["d"] = {k: v + [x] for (k, v), x in zip(PROJECTS[0]["d"].items(), [
    "Typical middle-section design: about 25 m × 6 m, linked by module-transfer robots, with curing tunnel ovens, automatic screw-driving with torque and angle monitoring, AOI and label printing.",
    "Thiết kế đoạn giữa điển hình: khoảng 25 m × 6 m, nối bằng robot chuyển mô-đun, có lò sấy đường hầm, bắt vít tự động giám sát mô-men và góc, AOI và in nhãn.",
    "中段典型方案：约 25 米 × 6 米，由模组搬运机械手串联，含固化隧道炉、带扭矩与角度监控的自动锁螺丝、AOI 检测与自动贴标。"])}
PROJECTS[1]["vid"] = "E01"
PROJECTS[2]["vid"] = "B01"
PROJECTS.insert(1, {"vid": "D02", "imgs": [],
    "t": {"en": "Automotive air-PTC heater cores: automatic production line, commissioned on site", "vi": "Lõi sưởi PTC không khí cho ô tô: dây chuyền tự động, chạy thử tại nhà máy khách hàng", "zh": "汽车暖风 PTC 发热芯：自动生产线（客户现场调试）"},
    "ind": {"en": "EV & automotive", "vi": "Xe điện & ô tô", "zh": "新能源与汽车"},
    "d": {"en": ["Automatic production of corrugated-fin heater cores for vehicle cabin heating.", "A companion assembly line for heater units was commissioned at the customer's plant by our engineers.", "Both lines carry part tracking from station to station."],
          "vi": ["Sản xuất tự động lõi sưởi dạng lá sóng cho hệ thống sưởi cabin ô tô.", "Dây chuyền lắp ráp bộ sưởi đi kèm đã được kỹ sư của chúng tôi chạy thử tại nhà máy khách hàng.", "Cả hai dây chuyền đều theo dõi sản phẩm qua từng trạm."],
          "zh": ["自动生产车用暖风波纹条发热芯。", "配套的发热组件组装线由我们的工程师在客户现场完成调试。", "两条线都在工位间追踪产品。"]}})
PROJECTS.insert(4, {"vid": "C01", "imgs": [],
    "t": {"en": "Cosmetic packaging: lipstick mechanism assembly and cap hot stamping", "vi": "Bao bì mỹ phẩm: lắp ráp cơ cấu son môi và ép nhũ nắp", "zh": "化妆品包材：口红推出组件组立与瓶盖烫金"},
    "ind": {"en": "Cosmetic packaging", "vi": "Bao bì mỹ phẩm", "zh": "化妆品包材"},
    "d": {"en": ["Automatic assembly of lipstick swivel mechanisms from bowl-fed parts.", "Automatic hot stamping of round pump caps and shaped mascara caps.", "Pad-printing and rotary screen-printing machines for decoration."],
          "vi": ["Lắp ráp tự động cơ cấu xoay son môi từ chi tiết cấp bằng phễu rung.", "Ép nhũ nóng tự động cho nắp bơm tròn và nắp mascara dạng đặc biệt.", "Máy in tampon và in lụa bàn xoay để trang trí."],
          "zh": ["振动盘供料，自动组立口红推出组件。", "圆形泵盖与异形睫毛膏盖自动烫金。", "配套移印机与转盘丝印机用于装饰印刷。"]}})
for _ind in INDUSTRIES:  # sharper stills from the new footage for the industry tiles
    _ind["vimg"] = {"appliances": "video/B01.jpg", "locks": "video/E01.jpg", "ev": "video/D01.jpg", "packaging": "video/C02.jpg"}.get(_ind["id"])
