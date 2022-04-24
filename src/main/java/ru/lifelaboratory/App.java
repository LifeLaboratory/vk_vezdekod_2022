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

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Random;

class App {

    public static void main(String[] args) throws ApiException, ClientException, InterruptedException {
        TransportClient transportClient = new HttpTransportClient();
        VkApiClient vk = new VkApiClient(transportClient);

        GroupActor actor = new GroupActor(212881098, "6bec718902959df1c1db2a96f16d4e3d5ab46d798af5b02a60e4768c6011112ec55b9cc9f22eefbe58902");
        Integer ts = vk.messages().getLongPollServer(actor).execute().getTs();

        ServiceActor serviceActor = new ServiceActor(8147140, "lcRNF9VZvIXLo2hW6xMj", "d9441aced9441aced9441aceb9d9384a0add944d9441acebb211889bb22cd6337e1ec90");
        List<Photo> photoAlbum = vk.photos().get(serviceActor).ownerId(-212881098).albumId("283784379").execute().getItems();

        while (true) {
            MessagesGetLongPollHistoryQuery historyQuery = vk.messages().getLongPollHistory(actor).ts(ts);
            List<Message> messageList = historyQuery.execute().getMessages().getItems();
            messageList.forEach(message -> {
                Random random = new Random();
                if (message.getText().equals("Старт")) {
                    try {
                        Collections.shuffle(photoAlbum);
                        List<Integer> tmp = new LinkedList<>();
                        for (int i = 0; i < 5; i++) {
                            tmp.add(photoAlbum.get(i).getId());
                        }
                        vk.messages()
                                .send(actor)
                                .userId(message.getFromId())
                                .randomId(random.nextInt(1000))
                                .attachment("photo-212881098_" + tmp.get(0)
                                        + ",photo-212881098_" + tmp.get(1)
                                        + ",photo-212881098_" + tmp.get(2)
                                        + ",photo-212881098_" + tmp.get(3)
                                        + ",photo-212881098_" + tmp.get(4))
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
