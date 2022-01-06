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
                {id:1, title: "Example", url: "/player/?url=example", src: "/img/example/0001.png"}
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