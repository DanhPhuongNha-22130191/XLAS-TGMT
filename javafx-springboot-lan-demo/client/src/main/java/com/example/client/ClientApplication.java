package com.example.client;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.util.concurrent.CompletableFuture;

public class ClientApplication extends Application {

    private final HttpClient httpClient = HttpClient.newBuilder()
            .version(HttpClient.Version.HTTP_2)
            .connectTimeout(Duration.ofSeconds(10))
            .build();

    private ChatService chatService;
    private TextArea chatArea;
    private TextField messageInput;
    private Button sendButton;

    private TextField ipField;
    private TextArea outputArea;
    private Button pingButton;

    @Override
    public void start(Stage stage) {
        stage.setTitle("LAN Ping & Chat Client (Khách)");

        Label instructionLabel = new Label("Nhập IP Server LAN:");
        ipField = new TextField("192.168.50.132");
        pingButton = new Button("Kết nối & Ping");

        outputArea = new TextArea();
        outputArea.setEditable(false);
        outputArea.setPrefHeight(100);
        outputArea.setPromptText("Log hệ thống...");

        // Chat UI
        Label chatLabel = new Label("Phòng Chat:");
        chatArea = new TextArea();
        chatArea.setEditable(false);
        chatArea.setPrefHeight(200);
        chatArea.setWrapText(true);

        messageInput = new TextField();
        messageInput.setPromptText("Nhập tin nhắn...");
        sendButton = new Button("Gửi");
        sendButton.setDisable(true); // Disable until connected

        pingButton.setOnAction(e -> doConnectAndPing());
        sendButton.setOnAction(e -> sendMessage());
        messageInput.setOnAction(e -> sendMessage()); // Enter to send

        VBox chatBox = new VBox(5, chatLabel, chatArea, new HBox(5, messageInput, sendButton));

        VBox root = new VBox(10);
        root.setPadding(new Insets(20));
        root.setAlignment(Pos.CENTER_LEFT);
        root.getChildren().addAll(instructionLabel, ipField, pingButton, new Label("Ping Log:"), outputArea,
                new Separator(), chatBox);

        // Init ChatService
        chatService = new ChatService(msg -> Platform.runLater(() -> chatArea.appendText(msg + "\n")));

        Scene scene = new Scene(root, 400, 600);
        stage.setScene(scene);
        stage.show();
    }

    private void doConnectAndPing() {
        String ip = ipField.getText().trim();
        if (ip.isEmpty()) {
            outputArea.appendText("Lỗi: Địa chỉ IP không được để trống.\n");
            return;
        }

        // 1. Ping (HTTP)
        doPing(ip);

        // 2. Connect Chat (WebSocket)
        outputArea.appendText("Đang kết nối Chat tới " + ip + "...\n");
        chatService.connect(ip);
        sendButton.setDisable(false);
    }

    private void sendMessage() {
        String msg = messageInput.getText().trim();
        if (!msg.isEmpty()) {
            chatService.sendMessage(msg);
            messageInput.clear();
        }
    }

    private void doPing(String ip) {
        String url = "http://" + ip + ":8080/api/ping";
        outputArea.appendText("HTTP Ping: " + url + " ...\n");

        HttpRequest request = HttpRequest.newBuilder()
                .GET()
                .uri(URI.create(url))
                .timeout(Duration.ofSeconds(5))
                .header("Accept", "text/plain")
                .build();

        CompletableFuture<HttpResponse<String>> responseFuture = httpClient.sendAsync(request,
                HttpResponse.BodyHandlers.ofString());

        responseFuture.thenAccept(response -> {
            Platform.runLater(() -> {
                if (response.statusCode() == 200) {
                    outputArea.appendText("Ping OK: " + response.body() + "\n");
                } else {
                    outputArea.appendText("Ping Lỗi: HTTP " + response.statusCode() + "\n");
                }
            });
        }).exceptionally(ex -> {
            Platform.runLater(() -> outputArea.appendText("Ping Lỗi: " + ex.getMessage() + "\n"));
            return null;
        });
    }

    public static void main(String[] args) {
        launch();
    }
}
