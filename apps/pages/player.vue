<template>
    <div class="container">
        <vs-row>
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12">
                <h1>{{ $route.query.url }}</h1>
            </vs-col>
        </vs-row>
        <vs-row>
            <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12">
                <div class="video-wrapper">
                    <video ref="videoPlayer" class="video-js vjs-theme-fantasy" playsinline width="500">
                        <source id="video-m3u8" type="application/x-mpegURL" />
                    </video>
                </div> 
            </vs-col>
        </vs-row>
    </div>
</template>
<script>
import videojs from 'video.js';
import "video.js/dist/video-js.css";
import '@videojs/themes/dist/fantasy/index.css';

export default {
    name: 'player',

    data() {
        return {
            player: null
        }
    },

    mounted() {
        var url = "/video/" + this.$route.query.url + "/video.m3u8";

        var video = document.getElementById('video-m3u8');
        video.src = url

        this.player = videojs(this.$refs.videoPlayer, {autoPlay: true, controls: true}, () => {console.log('onPlayerReady')});
    },

    beforeDestroy() {
        if(this.player) {
            this.player.dispose()
        }
    }
}
</script>
<style scoped>
.container {
    width: 80vw;
    margin: 0 auto;
}

.video-wrapper {
    padding-top: 20px;
    /* height: 80%; */
    width: 80vw;
    margin: 0 auto;
}

.video-wrapper video {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translateX(-50%) translateY(-50%);
    width: 80%;
    height: 80%;
    /* height: 100%; */
}
</style>