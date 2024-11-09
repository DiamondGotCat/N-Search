<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>N-Search - Next Generation Search Engine</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Marked.js -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        body {
            min-height: 100vh;
            padding-top: 60px; /* ヘッダーの高さ分の余白 */
            margin-bottom: 200px; /* 統合コンテナのスペース確保 */
        }
        /* フッターのスタイル */
        .footer {
            background-color: #fff;
            padding: 1em 0;
            text-align: center;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
        /* 検索ボックスとボタンを左下に固定（幅が広いデバイス向け） */
        .search-container {
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: stretch;
            padding: 15px;
            position: fixed;
            bottom: 20px;
            left: 20px;
            right: 20px;
            max-width: 400px;
            width: calc(100% - 40px);
            background-color: #fff;
            border-radius: 8px;
            z-index: 1000;
        }
        @media (min-width: 576px) {
            .search-container {
                left: 20px;
                right: auto;
            }
        }
        /* 検索結果を全画面表示 */
        #search-results {
            position: fixed;
            top: 60px; /* ヘッダーの下から開始 */
            left: 0;
            width: 100%;
            height: calc(100% - 60px);
            overflow-y: auto;
            padding: 20px;
            z-index: 999;
            display: none;
        }
        .result-item {
            padding: 20px;
            border-bottom: 1px solid #e0e0e0;
        }
        .result-item:last-child {
            border-bottom: none;
        }
        .url {
            word-break: break-all;
            color: #6c757d;
            font-size: 0.875em;
        }
        /* チャットコンテナ（幅が広いデバイス向け） */
        .chat-container {
            position: fixed;
            right: 20px;
            bottom: 20px;
            width: 100%;
            max-width: 500px;
            max-height: 80vh;
            overflow-y: auto;
            background-color: #fff;
            padding: 15px;
            border-radius: 8px;
            z-index: 1000;
        }
        @media (max-width: 575.98px) {
            /* 幅が狭いデバイス向けのスタイル */
            .chat-container {
                display: none;
            }
            .search-container {
                display: none;
            }
            /* 統合コンテナのスタイル */
            .unified-container {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                max-height: 50vh;
                background-color: #fff;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                z-index: 1500;
                display: flex;
                flex-direction: column;
                transition: max-height 0.3s ease;
            }
            .unified-container.expanded {
                max-height: 80vh;
            }
            /* グリップのスタイル */
            .grip {
                width: 40px;
                height: 5px;
                background-color: #ccc;
                border-radius: 3px;
                margin: 10px auto;
                cursor: ns-resize;
            }
            /* 統合コンテナ内のコンテンツ */
            .unified-content {
                flex: 1;
                overflow-y: auto;
                padding: 10px 15px 15px 15px;
            }
        }
        .chat-messages {
            max-height: 60vh;
            overflow-y: auto;
            margin-bottom: 10px;
        }
        .chat-message {
            margin-bottom: 10px;
        }
        .chat-message.user {
            text-align: right;
        }
        .chat-message.assistant {
            text-align: left;
        }
        /* モーダルのオーバーレイを調整 */
        .modal {
            z-index: 2000;
        }
    </style>
</head>
<body>
    <!-- ナビゲーションバー -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white fixed-top">
        <div class="container-fluid">
            <a class="navbar-brand fw-bold" href="#">N-Search with AI</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarBasic" aria-controls="navbarBasic" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarBasic">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <span class="nav-link text-muted">
                            AI may provide inaccurate responses in some cases. Please verify the content before referencing it.
                        </span>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" id="open-add-url-modal">
                            <i class="fas fa-plus me-1"></i> Add Site
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- 検索バーと検索ボタンを左下に配置（幅が広いデバイス向け） -->
    <div class="search-container d-none d-sm-flex">
        <div class="input-group mb-2">
            <input id="search-query" type="text" class="form-control" placeholder="Enter search query">
            <button id="search-button" class="btn btn-primary">
                <i class="fas fa-search me-2"></i> Search
            </button>
        </div>
        <div id="search-message" class="text-center mt-2"></div>
    </div>

    <!-- 検索結果を全画面で表示 -->
    <div id="search-results" class="container">
        <div class="row">
            <div class="col-12">
                <h2 class="h4 mb-4">Search Results (Sorting by all-MiniLM-L6-v2: ON)</h2>
                <div id="results-list"></div>
            </div>
        </div>
    </div>

    <!-- Ask AI Container（幅が広いデバイス向け） -->
    <div id="ask-ai-container" class="chat-container rounded d-none d-sm-block">
        <div class="mb-3">
            <label for="model-select" class="form-label"><h5>Select Model</h5></label>
            <select id="model-select" class="form-select">
                <option value="">Select a model</option>
            </select>
        </div>
        <div id="chat-box">
            <div id="chat-messages" class="chat-messages"></div>
            <div class="input-group">
                <textarea id="ask-ai-query" class="form-control" placeholder="Ask in Natural Language?" rows="1"></textarea>
                <button id="ask-ai-button" class="btn btn-info">
                    <i class="fas fa-paper-plane me-1"></i> Send
                </button>
                <button id="continue-ai-button" class="btn btn-success d-none" title="Continue">
                    <i class="fas fa-plus"></i>
                </button>
                <button id="clear-ai-button" class="btn btn-danger" title="Clear">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
        </div>
    </div>

    <!-- 統合コンテナ（幅が狭いデバイス向け） -->
    <div class="unified-container d-block d-sm-none">
        <!-- グリップ -->
        <div class="grip"></div>
        <!-- 統合コンテンツ -->
        <div class="unified-content">
            <!-- 検索バー -->
            <div class="mb-3">
                <div class="input-group">
                    <input id="search-query-mobile" type="text" class="form-control" placeholder="検索クエリを入力">
                    <button id="search-button-mobile" class="btn btn-primary">
                        <i class="fas fa-search me-2"></i> Search
                    </button>
                </div>
                <div id="search-message-mobile" class="text-center mt-2"></div>
            </div>
            <!-- 検索結果 -->
            <div id="search-results-mobile" class="mb-3" style="display: none;">
                <h5 class="mb-3">Search Results (Sorting by all-MiniLM-L6-v2: ON)</h5>
                <div id="results-list-mobile"></div>
            </div>
            <!-- AIチャット -->
            <div id="ask-ai-container-mobile" class="chat-container-mobile rounded">
                <div class="mb-3">
                    <label for="model-select" class="form-label"><h5>Select Model</h5></label>
                    <select id="model-select" class="form-select">
                        <option value="">Select a model</option>
                    </select>
                </div>
                <div id="chat-box-mobile">
                    <div id="chat-messages-mobile" class="chat-messages"></div>
                    <div class="input-group">
                        <textarea id="ask-ai-query-mobile" class="form-control" placeholder="日本語で聞いてみる？" rows="1"></textarea>
                        <button id="ask-ai-button-mobile" class="btn btn-info">
                            <i class="fas fa-paper-plane me-1"></i> Send
                        </button>
                        <button id="continue-ai-button-mobile" class="btn btn-success d-none" title="Continue">
                            <i class="fas fa-plus"></i>
                        </button>
                        <button id="clear-ai-button-mobile" class="btn btn-danger" title="Clear">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Add URL Modal -->
    <div class="modal fade" id="add-url-modal" tabindex="-1" aria-labelledby="addUrlModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 id="addUrlModalLabel" class="modal-title">Add Site</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="mb-3">
                        <label for="add-url-input" class="form-label">URL</label>
                        <input type="url" class="form-control" id="add-url-input" placeholder="https://example.com">
                    </div>
                </div>
                <div class="modal-footer">
                    <button id="save-url-button" type="button" class="btn btn-success">Request</button>
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS and dependencies (Popper) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Add URL Modal Logic
            const addUrlModal = new bootstrap.Modal(document.getElementById('add-url-modal'));
            const openAddUrlModalButton = document.getElementById('open-add-url-modal');
            const saveUrlButton = document.getElementById('save-url-button');
            const addUrlInput = document.getElementById('add-url-input');
            const modelSelect = document.getElementById('model-select');

            // Open the modal
            openAddUrlModalButton.addEventListener('click', (e) => {
                e.preventDefault(); // Prevent default anchor behavior
                addUrlModal.show();
            });

            // Save URL
            saveUrlButton.addEventListener('click', async () => {
                const url = addUrlInput.value.trim();
                if (!url) {
                    alert("Please enter a URL.");
                    return;
                }

                try {
                    // JSON形式でURLを送信
                    const response = await fetch(`http://${window.location.hostname}:3000/crawl-api`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ url })
                    });

                    if (response.ok) {
                        alert("Site added!");
                        addUrlModal.hide();
                        addUrlInput.value = '';
                    } else {
                        const errorData = await response.json();
                        alert(`Failed to add site: ${errorData.error || response.statusText}`);
                    }
                } catch (error) {
                    console.error("Site add error:", error);
                    alert(`Failed to add site: ${error.message}`);
                }
            });

            // 検索機能（幅が広いデバイス向け）
            const searchButton = document.getElementById('search-button');
            const searchQueryInput = document.getElementById('search-query');
            const searchResultsDiv = document.getElementById('search-results');
            const resultsList = document.getElementById('results-list');
            const searchMessage = document.getElementById('search-message');

            searchButton.addEventListener('click', async () => {
                const query = searchQueryInput.value.trim();
                if (!query) {
                    searchMessage.innerHTML = '<p class="text-danger">Please enter a query.</p>';
                    return;
                }

                searchMessage.innerHTML = '<p>Searching...</p>';
                searchResultsDiv.style.display = 'none';
                resultsList.innerHTML = '';

                try {
                    const response = await fetch(`http://${window.location.hostname}:3000/search-api/?q=${encodeURIComponent(query)}`);
                    if (!response.ok) {
                        throw new Error(`Server error: ${response.statusText}`);
                    }
                    const data = await response.json();
                    searchMessage.innerHTML = '';

                    if (data.results.length === 0) {
                        searchMessage.innerHTML = `
                            <p class="text-danger">No results found.</p>
                            <p>Use AI at the bottom left to access sites not in the database.</p>
                        `;
                        return;
                    }

                    data.results.forEach(doc => {
                        const item = document.createElement('div');
                        item.classList.add('result-item', 'border-bottom', 'pb-3', 'mb-3');

                        const title = document.createElement('h5');
                        title.classList.add('fw-bold');
                        title.innerHTML = `<a href="${doc.url}" target="_blank">${doc.title}</a>`;
                        item.appendChild(title);

                        const url = document.createElement('p');
                        url.classList.add('url');
                        url.textContent = doc.url;
                        item.appendChild(url);

                        const description = document.createElement('p');
                        description.textContent = doc.description;
                        item.appendChild(description);

                        resultsList.appendChild(item);
                    });

                    searchResultsDiv.style.display = 'block';
                } catch (error) {
                    console.error('Search error:', error);
                    searchMessage.innerHTML = `<p class="text-danger">Search error: ${error.message}</p>`;
                }
            });

            searchQueryInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    searchButton.click();
                }
            });

            // Ask AI機能（幅が広いデバイス向け）
            const askAiButton = document.getElementById('ask-ai-button');
            const continueAiButton = document.getElementById('continue-ai-button');
            const askAiQueryInput = document.getElementById('ask-ai-query');
            const chatMessagesDiv = document.getElementById('chat-messages');
            const clearAiButton = document.getElementById('clear-ai-button');
            
            let chatHistory = '';

            function showContinueButton() {
                continueAiButton.classList.remove('d-none');
            }

            async function fetchModels() {
                try {
                    const response = await fetch(`http://${window.location.hostname}:3000/models`);
                    if (!response.ok) {
                        throw new Error(`Error fetching models: ${response.statusText}`);
                    }
                    const models = await response.json();
                    models.forEach(model => {
                        const option = document.createElement('option');
                        option.value = model;
                        option.textContent = model;
                        modelSelect.appendChild(option);
                    });
                } catch (error) {
                    console.error('Error fetching models:', error);
                }
            }

            fetchModels();

            clearAiButton.addEventListener('click', () => {
                chatMessagesDiv.innerHTML = '';
                chatHistory = '';
                continueAiButton.classList.add('d-none');
            });

            askAiButton.addEventListener('click', async () => {
                const query = askAiQueryInput.value.trim();
                const selectedModel = modelSelect.value;

                if (!query) {
                    return;
                }

                // ユーザーメッセージをチャットに追加
                const userMessage = document.createElement('div');
                userMessage.classList.add('chat-message', 'user', 'bg-primary', 'text-white', 'p-2', 'rounded');
                userMessage.textContent = query;
                chatMessagesDiv.appendChild(userMessage);
                askAiQueryInput.value = '';

                // ユーザーメッセージをチャット履歴に追加
                chatHistory += `[user]${query}[/user]`;

                // 続けるボタンを表示
                showContinueButton();

                // スクロールを最下部に移動
                chatMessagesDiv.scrollTop = chatMessagesDiv.scrollHeight;

                try {
                    const response = await fetch(`http://${window.location.hostname}:3000/ask-ai`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            query: `[inst][/inst]${chatHistory}[assistant]`,
                            model: selectedModel
                        })
                    });

                    if (!response.ok) {
                        throw new Error(`サーバーエラー: ${response.statusText}`);
                    }

                    const data = await response.json();
                    const assistantMessage = document.createElement('div');
                    assistantMessage.classList.add('chat-message', 'assistant', 'bg-light', 'p-2', 'rounded');
                    assistantMessage.innerHTML = marked.parse(data.response);
                    chatMessagesDiv.appendChild(assistantMessage);

                    // アシスタントメッセージをチャット履歴に追加
                    chatHistory += `[assistant]${data.response}[/assistant]`;

                    // スクロールを最下部に移動
                    chatMessagesDiv.scrollTop = chatMessagesDiv.scrollHeight;

                } catch (error) {
                    const errorMessage = document.createElement('div');
                    errorMessage.classList.add('chat-message', 'assistant', 'text-danger');
                    errorMessage.textContent = `エラーが発生しました: ${error.message}`;
                    chatMessagesDiv.appendChild(errorMessage);

                    // スクロールを最下部に移動
                    chatMessagesDiv.scrollTop = chatMessagesDiv.scrollHeight;
                }
            });

            function removeLastChars(text, num) {
                return text.slice(0, -num);
            }

            continueAiButton.addEventListener('click', async () => {
                try {
                    const response = await fetch(`http://${window.location.hostname}:3000/ask-ai`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            query: `[inst][/inst]${removeLastChars(chatHistory,12)}`
                        })
                    });

                    if (!response.ok) {
                        throw new Error(`サーバーエラー: ${response.statusText}`);
                    }

                    const data = await response.json();
                    
                    // 最新の assistant メッセージ div を取得
                    const lastAssistantMessage = document.querySelector('#chat-messages .chat-message.assistant:last-of-type');
                    
                    if (lastAssistantMessage) {
                        // 内容を追加
                        lastAssistantMessage.innerHTML += marked.parse(data.response).trim();
                    } else {
                        // 新規作成
                        const newAssistantMessage = document.createElement('div');
                        newAssistantMessage.classList.add('chat-message', 'assistant', 'bg-light', 'p-2', 'rounded');
                        newAssistantMessage.innerHTML = marked.parse(data.response).trim();
                        chatMessagesDiv.appendChild(newAssistantMessage);
                    }

                    // チャット履歴に追加
                    chatHistory += `${data.response}[/assistant]`;

                    // スクロールを最下部に移動
                    chatMessagesDiv.scrollTop = chatMessagesDiv.scrollHeight;
                } catch (error) {
                    const errorMessage = document.createElement('div');
                    errorMessage.classList.add('chat-message', 'assistant', 'text-danger');
                    errorMessage.textContent = `エラーが発生しました: ${error.message}`;
                    chatMessagesDiv.appendChild(errorMessage);

                    // スクロールを最下部に移動
                    chatMessagesDiv.scrollTop = chatMessagesDiv.scrollHeight;
                }
            });

            /* 統合コンテナのドラッグによる高さ調整 */
            const unifiedContainer = document.querySelector('.unified-container');
            const grip = unifiedContainer.querySelector('.grip');
            let isDragging = false;
            let startY = 0;
            let startHeight = 0;

            grip.addEventListener('mousedown', (e) => {
                isDragging = true;
                startY = e.clientY;
                startHeight = unifiedContainer.offsetHeight;
                document.body.style.cursor = 'ns-resize';
                document.body.style.userSelect = 'none';
            });

            document.addEventListener('mousemove', (e) => {
                if (!isDragging) return;
                const dy = startY - e.clientY;
                let newHeight = startHeight + dy;
                const minHeight = 200; // 最小高さ
                const maxHeight = window.innerHeight * 0.9; // 最大高さ
                if (newHeight < minHeight) newHeight = minHeight;
                if (newHeight > maxHeight) newHeight = maxHeight;
                unifiedContainer.style.maxHeight = `${newHeight}px`;
            });

            document.addEventListener('mouseup', () => {
                if (isDragging) {
                    isDragging = false;
                    document.body.style.cursor = 'default';
                    document.body.style.userSelect = 'auto';
                }
            });

            /* タッチイベント対応 */
            grip.addEventListener('touchstart', (e) => {
                isDragging = true;
                startY = e.touches[0].clientY;
                startHeight = unifiedContainer.offsetHeight;
                document.body.style.cursor = 'ns-resize';
                document.body.style.userSelect = 'none';
            });

            document.addEventListener('touchmove', (e) => {
                if (!isDragging) return;
                const dy = startY - e.touches[0].clientY;
                let newHeight = startHeight + dy;
                const minHeight = 200; // 最小高さ
                const maxHeight = window.innerHeight * 0.9; // 最大高さ
                if (newHeight < minHeight) newHeight = minHeight;
                if (newHeight > maxHeight) newHeight = maxHeight;
                unifiedContainer.style.maxHeight = `${newHeight}px`;
            });

            document.addEventListener('touchend', () => {
                if (isDragging) {
                    isDragging = false;
                    document.body.style.cursor = 'default';
                    document.body.style.userSelect = 'auto';
                }
            });

            /* 統合コンテナ用の検索機能 */
            const searchButtonMobile = document.getElementById('search-button-mobile');
            const searchQueryInputMobile = document.getElementById('search-query-mobile');
            const searchResultsMobileDiv = document.getElementById('search-results-mobile');
            const resultsListMobile = document.getElementById('results-list-mobile');
            const searchMessageMobile = document.getElementById('search-message-mobile');

            searchButtonMobile.addEventListener('click', async () => {
                const query = searchQueryInputMobile.value.trim();
                if (!query) {
                    searchMessageMobile.innerHTML = '<p class="text-danger">クエリを入力してください。</p>';
                    return;
                }

                searchMessageMobile.innerHTML = '<p>検索中...</p>';
                searchResultsMobileDiv.style.display = 'none';
                resultsListMobile.innerHTML = '';

                try {
                    const response = await fetch(`http://${window.location.hostname}:3000/search-api/?q=${encodeURIComponent(query)}`);
                    if (!response.ok) {
                        throw new Error(`サーバーエラー: ${response.statusText}`);
                    }
                    const data = await response.json();
                    searchMessageMobile.innerHTML = '';

                    if (data.results.length === 0) {
                        searchMessageMobile.innerHTML = `
                            <p class="text-danger">結果が見つかりませんでした。</p>
                            <p>AIを使用すると、<br>データベースにないサイトにアクセスできます。</p>
                        `;
                        return;
                    }

                    data.results.forEach(doc => {
                        const item = document.createElement('div');
                        item.classList.add('result-item', 'border-bottom', 'pb-3', 'mb-3');

                        const title = document.createElement('h5');
                        title.classList.add('fw-bold');
                        title.innerHTML = `<a href="${doc.url}" target="_blank">${doc.title}</a>`;
                        item.appendChild(title);

                        const url = document.createElement('p');
                        url.classList.add('url');
                        url.textContent = doc.url;
                        item.appendChild(url);

                        const description = document.createElement('p');
                        description.textContent = doc.description;
                        item.appendChild(description);

                        resultsListMobile.appendChild(item);
                    });

                    searchResultsMobileDiv.style.display = 'block';
                } catch (error) {
                    console.error('検索エラー:', error);
                    searchMessageMobile.innerHTML = `<p class="text-danger">検索中にエラーが発生しました: ${error.message}</p>`;
                }
            });

            searchQueryInputMobile.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    searchButtonMobile.click();
                }
            });

            /* 統合コンテナ用のAsk AI機能 */
            const askAiButtonMobile = document.getElementById('ask-ai-button-mobile');
            const continueAiButtonMobile = document.getElementById('continue-ai-button-mobile');
            const askAiQueryInputMobile = document.getElementById('ask-ai-query-mobile');
            const chatMessagesMobileDiv = document.getElementById('chat-messages-mobile');
            const clearAiButtonMobile = document.getElementById('clear-ai-button-mobile');

            let chatHistoryMobile = '';

            function showContinueButtonMobile() {
                continueAiButtonMobile.classList.remove('d-none');
            }

            clearAiButtonMobile.addEventListener('click', () => {
                chatMessagesMobileDiv.innerHTML = '';
                chatHistoryMobile = '';
                continueAiButtonMobile.classList.add('d-none');
            });

            askAiButtonMobile.addEventListener('click', async () => {
                const query = askAiQueryInputMobile.value.trim();
                if (!query) {
                    return;
                }

                // ユーザーメッセージをチャットに追加
                const userMessage = document.createElement('div');
                userMessage.classList.add('chat-message', 'user', 'bg-primary', 'text-white', 'p-2', 'rounded');
                userMessage.textContent = query;
                chatMessagesMobileDiv.appendChild(userMessage);
                askAiQueryInputMobile.value = '';

                // ユーザーメッセージをチャット履歴に追加
                chatHistoryMobile += `[user]${query}[/user]`;

                // 続けるボタンを表示
                showContinueButtonMobile();

                // スクロールを最下部に移動
                chatMessagesMobileDiv.scrollTop = chatMessagesMobileDiv.scrollHeight;

                try {
                    const response = await fetch(`http://${window.location.hostname}:3000/ask-ai`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            query: `[inst][/inst]${chatHistoryMobile}[assistant]`
                        })
                    });

                    if (!response.ok) {
                        throw new Error(`サーバーエラー: ${response.statusText}`);
                    }

                    const data = await response.json();
                    const assistantMessage = document.createElement('div');
                    assistantMessage.classList.add('chat-message', 'assistant', 'bg-light', 'p-2', 'rounded');
                    assistantMessage.innerHTML = marked.parse(data.response);
                    chatMessagesMobileDiv.appendChild(assistantMessage);

                    // アシスタントメッセージをチャット履歴に追加
                    chatHistoryMobile += `[assistant]${data.response}[/assistant]`;

                    // スクロールを最下部に移動
                    chatMessagesMobileDiv.scrollTop = chatMessagesMobileDiv.scrollHeight;

                } catch (error) {
                    const errorMessage = document.createElement('div');
                    errorMessage.classList.add('chat-message', 'assistant', 'text-danger');
                    errorMessage.textContent = `エラーが発生しました: ${error.message}`;
                    chatMessagesMobileDiv.appendChild(errorMessage);

                    // スクロールを最下部に移動
                    chatMessagesMobileDiv.scrollTop = chatMessagesMobileDiv.scrollHeight;
                }
            });

            function removeLastCharsMobile(text, num) {
                return text.slice(0, -num);
            }

            continueAiButtonMobile.addEventListener('click', async () => {
                try {
                    const response = await fetch(`http://${window.location.hostname}:3000/ask-ai`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            query: `[inst][/inst]${removeLastCharsMobile(chatHistoryMobile,12)}`
                        })
                    });

                    if (!response.ok) {
                        throw new Error(`サーバーエラー: ${response.statusText}`);
                    }

                    const data = await response.json();
                    
                    // 最新の assistant メッセージ div を取得
                    const lastAssistantMessageMobile = document.querySelector('#chat-messages-mobile .chat-message.assistant:last-of-type');
                    
                    if (lastAssistantMessageMobile) {
                        // 内容を追加
                        lastAssistantMessageMobile.innerHTML += marked.parse(data.response).trim();
                    } else {
                        // 新規作成
                        const newAssistantMessage = document.createElement('div');
                        newAssistantMessage.classList.add('chat-message', 'assistant', 'bg-light', 'p-2', 'rounded');
                        newAssistantMessage.innerHTML = marked.parse(data.response).trim();
                        chatMessagesMobileDiv.appendChild(newAssistantMessage);
                    }

                    // チャット履歴に追加
                    chatHistoryMobile += `${data.response}[/assistant]`;

                    // スクロールを最下部に移動
                    chatMessagesMobileDiv.scrollTop = chatMessagesMobileDiv.scrollHeight;
                } catch (error) {
                    const errorMessage = document.createElement('div');
                    errorMessage.classList.add('chat-message', 'assistant', 'text-danger');
                    errorMessage.textContent = `エラーが発生しました: ${error.message}`;
                    chatMessagesMobileDiv.appendChild(errorMessage);

                    // スクロールを最下部に移動
                    chatMessagesMobileDiv.scrollTop = chatMessagesMobileDiv.scrollHeight;
                }
            });
        });
    </script>
</body>
</html>
