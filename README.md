# Swamp Izzo 音效板 🩸

ALIVV ALIVV 🗣️ 桌面音效板嚟架啦

九個掣 🔥 九個聲 🔥 熱鍵死做爛做 😈

macOS Windows 兩樣都掂 💫 撳掣或者撳 1-9 WHAT WHAT 🧛‍♂️

## 功能特點 🔥

- **全局熱鍵**: 數字鍵 1-9 同埋數字鍵盤死做爛做 🗣️ 就算用緊其他 apps 都 work
- **Type B 循環播放**: 每個鍵不停循環播音頻片段 💫
- **玻璃風格介面**: 現代化置頂視窗 PNG 資源 🖤
- **低延遲音頻**: 緩存緩存緩存 🩸 即時播放
- **背景運行**: 繼續運行運行運行你做其他嘢都得 😈
- **系統托盤**: 最小化到托盤 🧛‍♂️
- **易於安裝**: Windows 安裝程式同埋 macOS DMG WHAT 🔥

## 安裝方法 🗣️

### macOS

1. 去 GitHub Releases 攞嘢 🔥
2. 下載 SwampIzzo.dmg WHAT WHAT
3. 拖個 app 去 Applications 資料夾 💫
4. 打開 Applications 雙擊 Swamp Izzo 🧛‍♂️
5. 安全提示彈出撳 Open okay okay OKAY 😈
6. 輔助功能權限要俾埋佢 🩸

#### macOS 輔助功能設定（如果冇提示）

1. 系統偏好設定 安全與隱私 輔助功能 🔥
2. 撳個鎖解鎖 🗣️
3. 撳 "+" 揀 Swamp Izzo 💫
4. 重新啟動 app ALIVV ALIVV 🖤

### Windows

1. GitHub Releases 下載下載 🔥
2. 攞 SwampIzzoSoundboard_Setup.exe 安裝程式 WHAT
3. 右鍵撳安裝程式 "以系統管理員身分執行" OKAY 🗣️
4. 跟住提示做做做 😈
5. 裝咗落 Program Files 𡃁 🩸
6. 開始選單或者執行檔 LETS GO 🔥

## 使用方法 🔥

### 啟動 App

- **macOS**: Applications 雙擊 Swamp Izzo 🗣️
- **Windows**: 開始選單捷徑或者執行檔 LETS GO 😈

### 觸發聲音 🩸

1. **熱鍵**: 撳 1-9 或者數字鍵盤 WHAT WHAT WHAT
   - 用緊其他 apps 都 work 💫
   - 每個鍵循環循環循環播音頻片段 🔥

2. **滑鼠點擊**: 撳音效板視窗嘅掣 ALIVV 🧛‍♂️

### 設定 🖤

編輯 config.json 喺 app 目錄度自訂自訂自訂 🗣️

- 每個鍵嘅音頻檔案路徑 🔥
- 按鈕標籤 💫
- 視窗大小 😈
- 片段重置計時器（閒置時間直到循環重置）🩸

設定檔範例：
```json
{
  "keys": {
    "1": {
      "label": "聲音 1",
      "clips": ["assets/audio/sound_1.wav", "assets/audio/alternate_1.wav"],
      "reset_seconds": 10
    }
  }
}
```

### 自訂音頻檔案 🔥

1. 將 WAV 檔案放入 assets/audio/ 🗣️
2. 編輯 config.json 參考你嘅檔案 💫
3. 重新啟動 app WHAT WHAT 😈
4. 撳鍵 ALIVV ALIVV 🩸

## 開發 Development

### 需求

- Python 3.10 或以上版本
- 虛擬環境（建議）

### 設定步驟

1. Clone 呢個 repository：
```bash
git clone https://github.com/ShrikarSwami/SwampIzzoSoundboard.git
cd SwampIzzoSoundboard
```

2. 建立同埋啟動虛擬環境：
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 安裝依賴套件：
```bash
pip install -r requirements.txt
```

4. 執行 app：
```bash
python -m src.app
```

### 專案結構

```
SwampIzzoSoundboard/
├── src/
│   ├── __init__.py          # 套件初始化
│   ├── app.py               # 主要 app 入口點同生命週期
│   ├── ui.py                # UI 視窗同元件
│   ├── audio.py             # 音頻播放同緩存
│   ├── config.py            # 設定載入同驗證
│   └── hotkeys.py           # 全局熱鍵監聽器
├── assets/
│   ├── ui/                  # UI 圖片（背景圖、按鈕、圖標）
│   │   └── icons/          # 應用程式圖標
│   └── audio/               # 音頻檔案
├── scripts/
│   ├── create_assets.py     # 生成 PNG 資源
│   ├── generate_audio.py    # 生成測試音頻檔案
│   ├── generate_png_assets.py # 生成 PNG UI 資源
│   ├── build_mac.sh         # macOS 建置腳本
│   └── build_win.ps1        # Windows 建置腳本
├── config.json              # 應用程式設定檔
├── swampizz_mac.spec        # PyInstaller spec for macOS
├── swampizz_windows.spec    # PyInstaller spec for Windows
├── installer_windows.iss    # Inno Setup 安裝程式腳本
└── requirements.txt         # Python 依賴套件
```

### 建置發佈版本

#### macOS

```bash
chmod +x build_mac.sh
./build_mac.sh
```

輸出：`dist/Swamp Izzo.app` 同埋可選 DMG

#### Windows

```powershell
.\build_win.ps1
```

輸出：`dist/swamp_izzo/` 目錄

建立安裝程式（需要 Inno Setup）：
```powershell
iscc installer_windows.iss
```

輸出：`dist/SwampIzzoSoundboard_Setup.exe`

## 故障排除 Troubleshooting

### macOS 全局熱鍵唔 work

Swamp Izzo 需要輔助功能權限先可以監聽全局熱鍵。

1. 打開系統偏好設定/設定
2. 去 安全與隱私 > 輔助功能
3. 將 Swamp Izzo app 加入清單
4. 重新啟動應用程式

### 音頻播唔到

1. 檢查音頻檔案係咪存在於 `config.json` 指定嘅路徑
2. 確認音頻檔案係有效嘅 WAV 格式
3. 檢查系統音量係咪靜音咗
4. 睇吓 `soundboard.log` 有冇錯誤訊息

### App 啟動時崩潰

1. 檢查 `soundboard.log` 睇錯誤詳情
2. 確保所有資源檔案都存在於正確位置
3. 確認安裝咗 Python 3.10+
4. 試吓重新安裝依賴套件：`pip install -r requirements.txt --force-reinstall`

## 音頻播放技術

呢個 app 支援多種音頻後端以達到最大兼容性：

1. **QMediaPlayer** (PySide6 內置，首選)
2. **sounddevice** (備用方案)

App 會喺運行時自動揀選最佳可用後端。

### 支援嘅音頻格式

- **WAV 檔案** (PCM，任何取樣率同位元深度)

## 效能 Performance

- **音頻緩存**：所有音頻檔案喺首次播放時緩存到記憶體入面以即時播放
- **非阻塞播放**：音頻喺背景執行緒播放唔會令 UI 卡住
- **反應靈敏 UI**：全局熱鍵同滑鼠點擊即時反應
- **低延遲**：優化至低於 100ms 觸發到聲音延遲

## 授權 License

呢個專案以原樣提供，供個人使用。

## 貢獻 Contributing

歡迎貢獻！歡迎提交 pull requests 或者開 issues 報告 bugs 同功能請求。

## 技術細節 Technical Details

### 全局熱鍵實現

使用 `pynput` 函式庫實現跨平台全局熱鍵支援：
- 監聽系統範圍嘅按鍵事件
- 將數字鍵盤同數字鍵 1-9 映射到回調函數
- 喺背景執行緒運行避免阻塞 UI

### 音頻實現

自訂音頻播放系統支援多個後端：
- **緩存**：載入音頻檔案一次並保留喺記憶體
- **非阻塞**：使用背景執行緒播放
- **多個後端**：自動選擇可用嘅音頻函式庫
- **跨平台**：可以喺 macOS、Windows 同 Linux 運行

### UI 架構

使用 PySide6 (Qt for Python) 建置：
- 無邊框、置頂視窗
- 基於 PNG 嘅玻璃風格 UI
- 系統托盤整合
- 反應式按鈕狀態

### 發佈方式

PyInstaller 將 app 打包成：
- **macOS**：.app bundle（可選：+ DMG 發佈）
- **Windows**：獨立目錄 + Inno Setup 安裝程式

## 系統需求 System Requirements

### macOS
- macOS 10.13 或以上版本
- 輔助功能權限（用於全局熱鍵）
- 音頻輸出裝置

### Windows
- Windows 10 或以上版本
- 系統管理員權限（安裝程式需要，可選）
- 音頻輸出裝置

## 已知限制 Known Limitations

1. **macOS**：需要輔助功能權限先可以用全局熱鍵
2. **音頻格式**：只支援 WAV 檔案（可輕易擴充）
3. **UI**：固定 420x420 視窗大小（可以喺程式碼度設定）
4. **按鍵**：限於數字鍵 1-9（可以喺程式碼度擴充）

## 未來改進計劃 Future Enhancements

- [ ] 支援 MP3 同 OGG 音頻格式
- [ ] 可自訂熱鍵（唔限於數字鍵）
- [ ] 每個鍵嘅音量控制
- [ ] 自訂 UI 主題
- [ ] 直接喺 app 內錄音
- [ ] 聲音堆疊（同時播放多個聲音）
- [ ] Linux 支援
