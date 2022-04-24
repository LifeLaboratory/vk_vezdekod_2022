package ru.lifelaboratory;

import com.vk.api.sdk.client.TransportClient;
import com.vk.api.sdk.client.VkApiClient;
import com.vk.api.sdk.client.actors.GroupActor;
import com.vk.api.sdk.client.actors.ServiceActor;
import com.vk.api.sdk.exceptions.ApiException;
import com.vk.api.sdk.exceptions.ClientException;
import com.vk.api.sdk.httpclient.HttpTransportClient;
import com.vk.api.sdk.objects.messages.Message;
import com.vk.api.sdk.objects.photos.Photo;
import com.vk.api.sdk.queries.messages.MessagesGetLongPollHistoryQuery;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class App {

    public static final String URL_REGEX = "^((https?|ftp)://|(www|ftp)\\.)?[a-z0-9-]+(\\.[a-z0-9-]+)+([/?].*)?$";

    public static void main(String[] args) throws ApiException, ClientException, InterruptedException {
        TransportClient transportClient = new HttpTransportClient();
        VkApiClient vk = new VkApiClient(transportClient);
        Map<Integer, Integer> userWord = new HashMap<>();
        Map<Integer, String> userAlbum = new HashMap<>();

        GroupActor actor = new GroupActor(212881098, "6bec718902959df1c1db2a96f16d4e3d5ab46d798af5b02a60e4768c6011112ec55b9cc9f22eefbe58902");
        Integer ts = vk.messages().getLongPollServer(actor).execute().getTs();

        ServiceActor serviceActor = new ServiceActor(8147140, "lcRNF9VZvIXLo2hW6xMj", "d9441aced9441aced9441aceb9d9384a0add944d9441acebb211889bb22cd6337e1ec90");

        while (true) {
            MessagesGetLongPollHistoryQuery historyQuery = vk.messages().getLongPollHistory(actor).ts(ts);
            List<Message> messageList = historyQuery.execute().getMessages().getItems();
            messageList.forEach(message -> {
                List<Photo> photoAlbum = null;
                try {
                    if (userAlbum.containsKey(message.getFromId())) {
                        photoAlbum = vk.photos().get(serviceActor)
                                .ownerId(Integer.valueOf(userAlbum.get(message.getFromId()).split("_")[0]))
                                .albumId(userAlbum.get(message.getFromId()).split("_")[1])
                                .execute().getItems();
                    } else {
                            photoAlbum = vk.photos().get(serviceActor)
                                    .ownerId(-212881098).albumId("283784379")
                                    .execute().getItems();
                    }
                } catch (ApiException | ClientException e) {
                    throw new RuntimeException(e);
                }

                Pattern p = Pattern.compile(URL_REGEX);
                Matcher matcher = p.matcher(message.getText());

                Random random = new Random();
                if (message.getText().equals("Старт")) {
                    try {
                        Collections.shuffle(photoAlbum);
                        String strForAttachment = "";
                        for (int i = 0; i < 5; i++) {
                            if (userAlbum.containsKey(message.getFromId())) {
                                strForAttachment += "photo"
                                        + Integer.valueOf(userAlbum.get(message.getFromId()).split("_")[0])
                                        + "_" + photoAlbum.get(i).getId() + ",";
                            } else {
                                strForAttachment += "photo-212881098_" + photoAlbum.get(i).getId() + ",";
                            }
                        }
                        vk.messages()
                                .send(actor)
                                .userId(message.getFromId())
                                .randomId(random.nextInt(1000))
                                .attachment(strForAttachment.substring(0, strForAttachment.length() - 1))
                                .execute();

                        int randomNumberOfImage = random.nextInt(5);
                        String[] randomImage = photoAlbum.get(randomNumberOfImage).getText().split(" ");
                        String word = randomImage[random.nextInt(randomImage.length)];
                        vk.messages()
                                .send(actor)
                                .userId(message.getFromId())
                                .randomId(random.nextInt(1000))
                                .message(word)
                                .execute();

                        userWord.put(message.getFromId(), randomNumberOfImage + 1);
                    } catch (ApiException | ClientException e) {
                        throw new RuntimeException(e);
                    }
                } else if (matcher.find()) {
                    userAlbum.put(message.getFromId(), message.getText().split("album")[1]);
                    try {
                        vk.messages()
                                .send(actor)
                                .userId(message.getFromId())
                                .randomId(random.nextInt(1000))
                                .message("Ваш альбом сменен")
                                .execute();
                    } catch (ApiException | ClientException e) {
                        throw new RuntimeException(e);
                    }
                } else if (userWord.containsKey(message.getFromId()) && userWord.get(message.getFromId()).toString().equals(message.getText())) {
                    try {
                        vk.messages()
                                .send(actor)
                                .userId(message.getFromId())
                                .randomId(random.nextInt(1000))
                                .message("+3 очка")
                                .execute();
                    } catch (ApiException | ClientException e) {
                        throw new RuntimeException(e);
                    }
                    userWord.remove(message.getFromId());
                } else if (userWord.containsKey(message.getFromId())) {
                    try {
                        vk.messages()
                                .send(actor)
                                .userId(message.getFromId())
                                .randomId(random.nextInt(1000))
                                .message("+0 очков")
                                .execute();
                    } catch (ApiException | ClientException e) {
                        throw new RuntimeException(e);
                    }
                }
            });
            ts = vk.messages().getLongPollServer(actor).execute().getTs();
            Thread.sleep(500);
        }


    }

}
