<template>
    <div class="container">
        <vs-row vs-justify="center">
            <vs-col class="card_row" type="flex" vs-justify="center" vs-w="3" v-for="item in items" :key="item.item">
                <nuxt-link :to="item.url">
                    <vs-card class="cardx">
                        <div slot="header"><h3>{{item.title}}</h3></div>
                        <div slot="media">
                            <img :src="item.src" />
                            </div>
                        <div>
                            <span>Lorem ipsum dolor sit amet.</span>
                        </div>
                    </vs-card>
                </nuxt-link>
            </vs-col>
        </vs-row>
    </div>
</template>
<script>
export default {
    data() {
        return {
            items: [
                {id:1, title: "動画1", url: "/player/?url=mio", src: "/img/mio/0018.png"},
                {id:2, title: "動画2", url: "/player/?url=cdefg", src: "/img/cdefg/0018.png"},
                {id:3, title: "動画3", url: "/player/?url=aya", src: "/img/aya/0018.png"}
            ]
        }
    }
}
</script>
<style>

.cardx {
    text-decoration: none;
    color: #020339;
}
.card_row {
    margin:1rem;
}
</style>