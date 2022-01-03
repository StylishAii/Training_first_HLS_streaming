<template>
    <div class="container">
        <vs-row>
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4">
                テキスト
            </vs-col>
        </vs-row>
        <vs-row>
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12">
                <h1>{{ $route.query.url }}</h1>
            </vs-col>
        </vs-row>
        <vs-row>
            <vs-col vs-type="flex" vs-justify="center" vs-w="12">
                <div class="video-wrapper">
                    <video id="video" controls></video>
                </div> 
            </vs-col>
        </vs-row>
    </div>
</template>
<script>
import Hls from 'hls.js';
export default {
    name: 'player',

    mounted() {
        var url = "/video/" + this.$route.query.url + "/video.m3u8";
        if (Hls.isSupported()) {
            var video = document.getElementById('video');
            var hls = new Hls();
            hls.attachMedia(video);
            hls.on(Hls.Events.MEDIA_ATTACHED, () => {
                hls.loadSource(url);
                hls.on(Hls.Events.MANIFEST_PARSED, (event, data) => {})
            })
        }
    }
}
</script>
<style scoped>
    .container {
        width: 80%;
        margin: 0 auto;
    }

    .video-wrapper {
        padding-top: 20px;
        height: 80%;
        margin: 0 auto;
    }

    video {
        display: block;
        width: 100%;
        height: 100%;
    }
</style>