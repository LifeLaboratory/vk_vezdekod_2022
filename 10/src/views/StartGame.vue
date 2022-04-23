<template>
    <div class="box">
        <div class="white_text">
            Для игры необходимо минимум 3 игрока
        </div>
        <a-form
            ref="formRef"
            name="dynamic_form_item"
            :model="dynamicValidateForm"
            v-bind="formItemLayoutWithOutLabel"
        >
            <a-form-item
            v-for="(domain, index) in dynamicValidateForm.domains"
            :key="domain.key"
            v-bind="formItemLayout"
            :name="['domains', index, 'value']"
            :rules="{
                required: true,
                message: 'domain can not be null',
                trigger: 'change',
            }"
            >
            <a-input
                v-model:value="domain.value"
                placeholder="Введите имя игрока"
                style="width: 60%; margin-right: 8px"
            />
            <MinusCircleOutlined
                v-show="dynamicValidateForm.domains.length > 1"
                class="dynamic-delete-button"
                :disabled="dynamicValidateForm.domains.length === 1"
                @click="removeDomain(domain)"
            />
            </a-form-item>
            <a-form-item v-bind="formItemLayoutWithOutLabel">
            <a-button type="dashed" style="width: 60%" @click="addDomain">
                <PlusOutlined />
                Добавить игрока
            </a-button>
            </a-form-item>
            <a-form-item v-bind="formItemLayoutWithOutLabel">
            <a-button type="primary" html-type="submit" @click="submitForm">Создать игру</a-button>
            </a-form-item>
        </a-form>
    </div>
</template>
<script>
import { MinusCircleOutlined, PlusOutlined } from '@ant-design/icons-vue';
import { defineComponent, reactive, ref } from 'vue';
import store from '@/store'
import router from '@/router'
function randomInteger(min, max) {
  // случайное число от min до (max+1)
  let rand = min + Math.random() * (max + 1 - min);
  return Math.floor(rand);
}
export default defineComponent({
  components: {
    MinusCircleOutlined,
    PlusOutlined,
  },

  setup() {
    const formRef = ref();
    const formItemLayout = {
      labelCol: {
        xs: {
          span: 0,
        },
        sm: {
          span: 0,
        },
      },
      wrapperCol: {
        xs: {
          span: 0,
        },
        sm: {
          span: 0,
        },
      },
    };
    const formItemLayoutWithOutLabel = {
      wrapperCol: {
        xs: {
          span: 0,
          offset: 0,
        },
        sm: {
          span: 0,
          offset: 0,
        },
      },
    };
    const dynamicValidateForm = reactive({
      domains: [],
    });
    
    const submitForm = () => {
      formRef.value.validate().then(() => {
        console.log('values', dynamicValidateForm.domains);
        if (dynamicValidateForm.domains.length < 3) {
            alert("В игре может быть минимум 3 игрока")
            return
        } else {
            let shpions = dynamicValidateForm.domains.length < 6 ? 1 : 2
            let listUser = [...dynamicValidateForm.domains]
            let a = []
            let lengthArray = dynamicValidateForm.domains.length
            try {
            for (let i = 0; i < lengthArray; i++) {
                try {
                    const randomInt = randomInteger(0, listUser.length - 1)
                    let randomUser = listUser[randomInt]
                    if (shpions != 0) {
                        randomUser.role = 1
                        shpions--
                    }
                    a.push(randomUser)
                    listUser.splice(randomInt, 1)
                }catch (e) {
                    console.log(e)
                }
            }
            } catch (er) {
                console.log(er)
            }
            console.log(a)
            
            store.commit('addUser', a)
            router.push('playGame')
        }
      }).catch(error => {
        console.log('error', error);
      });
    };

    const resetForm = () => {
      formRef.value.resetFields();
    };

    const removeDomain = item => {
      let index = dynamicValidateForm.domains.indexOf(item);

      if (index !== -1) {
        dynamicValidateForm.domains.splice(index, 1);
      }
    };

    const addDomain = () => {
      dynamicValidateForm.domains.push({
        value: '',
        key: Date.now(),
        role: 0
      });
    };

    return {
      formRef,
      formItemLayout,
      formItemLayoutWithOutLabel,
      dynamicValidateForm,
      submitForm,
      resetForm,
      removeDomain,
      addDomain,
    };
  },

});
</script>
<style>
.dynamic-delete-button {
  cursor: pointer;
  position: relative;
  top: 4px;
  font-size: 24px;
  color: white !important;
  transition: all 0.3s;
}
.dynamic-delete-button:hover {
  color: red;
}
.dynamic-delete-button[disabled] {
  cursor: not-allowed;
  opacity: 0.5;
}
</style>