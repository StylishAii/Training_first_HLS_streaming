<template>
    <div class="container">
        <vs-row vs-justify="center">
            <vs-col class="card_row" type="flex" vs-justify="center" vs-w="3" vs-sm="6" vs-xs="12" v-for="item in items" :key="item.item">
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
                {id:1, title: "ナースさん", url: "/player/?url=mio", src: "/img/mio/0018.png"},
                {id:2, title: "援交かわいい", url: "/player/?url=cdefg", src: "/img/cdefg/0018.png"},
                {id:3, title: "あやちゃん②", url: "/player/?url=aya", src: "/img/aya/0018.png"},
                {id:4, title: "愛乃まほろ ニット", url: "/player/?url=nti_bakunew", src: "/img/nti_bakunew/0018.png"},
                {id:5, title: "OL かわいい 無修正", url: "/player/?url=anmp", src: "/img/anmp/0018.png"},
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