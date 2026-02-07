package com.example.client;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.WebSocket;
import java.util.concurrent.CompletionStage;
import java.util.function.Consumer;

public class ChatService {

    private WebSocket webSocket;
    private final HttpClient client;
    private final Consumer<String> onMessageReceived;

    public ChatService(Consumer<String> onMessageReceived) {
        this.client = HttpClient.newHttpClient();
        this.onMessageReceived = onMessageReceived;
    }

    public void connect(String ip) {
        String wsUrl = "ws://" + ip + ":8080/ws/chat";
        client.newWebSocketBuilder()
                .buildAsync(URI.create(wsUrl), new WebSocketListener())
                .thenAccept(ws -> {
                    this.webSocket = ws;
                    onMessageReceived.accept("Kết nối Chat thành công!");
                })
                .exceptionally(ex -> {
                    onMessageReceived.accept("Lỗi kết nối Chat: " + ex.getMessage());
                    return null;
                });
    }

    public void sendMessage(String message) {
        if (webSocket != null) {
            webSocket.sendText(message, true);
        } else {
            onMessageReceived.accept("Chưa kết nối đến máy chủ Chat.");
        }
    }

    private class WebSocketListener implements WebSocket.Listener {
        @Override
        public void onOpen(WebSocket webSocket) {
            WebSocket.Listener.super.onOpen(webSocket);
        }

        @Override
        public CompletionStage<?> onText(WebSocket webSocket, CharSequence data, boolean last) {
            onMessageReceived.accept(data.toString());
            return WebSocket.Listener.super.onText(webSocket, data, last);
        }

        @Override
        public CompletionStage<?> onClose(WebSocket webSocket, int statusCode, String reason) {
            onMessageReceived.accept("Đã ngắt kết nối: " + reason);
            return WebSocket.Listener.super.onClose(webSocket, statusCode, reason);
        }

        @Override
        public void onError(WebSocket webSocket, Throwable error) {
            onMessageReceived.accept("Lỗi WebSocket: " + error.getMessage());
            WebSocket.Listener.super.onError(webSocket, error);
        }
    }
}
