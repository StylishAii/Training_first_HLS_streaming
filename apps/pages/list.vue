<template>
    <div class="container">
        <vs-row vs-justify="center">
            <vs-col class="card_row" type="flex" vs-justify="center" vs-w="3" vs-sm="6" vs-xs="12" v-for="item in this.shuffle(items)" :key="item.item">
                <nuxt-link :to="item.url" target="_blank">
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
            ]
        }
    },
    methods: {
        shuffle: function(array) {
            for (let i = array.length - 1; i >= 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
            return array;
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