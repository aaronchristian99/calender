<script setup>
  import { ref, computed, onMounted, useTemplateRef, watch } from "vue";
  import { Ckeditor } from "@ckeditor/ckeditor5-vue";
  import { ClassicEditor, AutoImage, Autosave, BalloonToolbar, Base64UploadAdapter, BlockQuote, Bold,
    CloudServices, Essentials, Heading, ImageBlock, ImageCaption, ImageInline, ImageInsert, ImageInsertViaUrl,
    ImageResize, ImageStyle, ImageTextAlternative, ImageToolbar, ImageUpload, Indent, IndentBlock, Italic, Link,
    LinkImage, MediaEmbed, Paragraph, Table, TableCaption, TableCellProperties, TableColumnResize, TableProperties,
    TableToolbar, Underline, WordCount } from 'ckeditor5';
  import VueDatePicker from "@vuepic/vue-datepicker";
  import "@vuepic/vue-datepicker/dist/main.css"
  import axios from "axios";
  import Button from "@/components/Button.vue";
  import Input from "@/components/Input.vue";
  import Location from "@/components/Location.vue";
  import Multiselect from "vue-multiselect";
  import "ckeditor5/ckeditor5.css";
  import "vue-multiselect/dist/vue-multiselect.min.css";
  import {useLoaderStore} from "@/stores/loader.js";
  import {useMessageStore} from "@/stores/message.js";

  const props = defineProps({
    isVisible: Boolean,
    event: Object
  });
  const emit = defineEmits(['toggle-form', 'update-events']);

  // Ckeditor configuration
  const LICENSE_KEY = 'GPL';
  // const editorMenuBar = useTemplateRef('editorMenuBarElement');
  const editorWordCount = useTemplateRef('editorWordCountElement');
  const isLayoutReady = ref(false);
  const editor = ClassicEditor;
  const config = computed(() => {
    if (!isLayoutReady.value) {
      return null;
    }

    return {
      toolbar: {
        items: [
          'heading',
          '|',
          'bold',
          'italic',
          'underline',
          '|',
          'link',
          'insertImage',
          'mediaEmbed',
          'insertTable',
          'blockQuote',
          '|',
          'outdent',
          'indent'
        ],
        shouldNotGroupWhenFull: false
      },
      plugins: [
        AutoImage,
        Autosave,
        BalloonToolbar,
        Base64UploadAdapter,
        BlockQuote,
        Bold,
        CloudServices,
        Essentials,
        Heading,
        ImageBlock,
        ImageCaption,
        ImageInline,
        ImageInsert,
        ImageInsertViaUrl,
        ImageResize,
        ImageStyle,
        ImageTextAlternative,
        ImageToolbar,
        ImageUpload,
        Indent,
        IndentBlock,
        Italic,
        Link,
        LinkImage,
        MediaEmbed,
        Paragraph,
        Table,
        TableCaption,
        TableCellProperties,
        TableColumnResize,
        TableProperties,
        TableToolbar,
        Underline,
        WordCount
      ],
      balloonToolbar: ['bold', 'italic', '|', 'link', 'insertImage'],
      heading: {
        options: [
          {
            model: 'paragraph',
            title: 'Paragraph',
            class: 'ck-heading_paragraph'
          },
          {
            model: 'heading1',
            view: 'h1',
            title: 'Heading 1',
            class: 'ck-heading_heading1'
          },
          {
            model: 'heading2',
            view: 'h2',
            title: 'Heading 2',
            class: 'ck-heading_heading2'
          },
          {
            model: 'heading3',
            view: 'h3',
            title: 'Heading 3',
            class: 'ck-heading_heading3'
          },
          {
            model: 'heading4',
            view: 'h4',
            title: 'Heading 4',
            class: 'ck-heading_heading4'
          },
          {
            model: 'heading5',
            view: 'h5',
            title: 'Heading 5',
            class: 'ck-heading_heading5'
          },
          {
            model: 'heading6',
            view: 'h6',
            title: 'Heading 6',
            class: 'ck-heading_heading6'
          }
        ]
      },
      image: {
        toolbar: [
          'toggleImageCaption',
          'imageTextAlternative',
          '|',
          'imageStyle:inline',
          'imageStyle:wrapText',
          'imageStyle:breakText',
          '|',
          'resizeImage'
        ]
      },
      initialData: '',
      licenseKey: LICENSE_KEY,
      link: {
        addTargetToExternalLinks: true,
        defaultProtocol: 'https://',
        decorators: {
          toggleDownloadable: {
            mode: 'manual',
            label: 'Downloadable',
            attributes: {
              download: 'file'
            }
          }
        }
      },
      placeholder: 'Type or paste your content here!',
      table: {
        contentToolbar: ['tableColumn', 'tableRow', 'mergeTableCells', 'tableProperties', 'tableCellProperties']
      }
    };
  });

  const event = ref({
    title: '',
    description: '',
    location: '',
    date: null,
    type: 'private',
    file: null,
    collaborators: []
  });
  const users = ref([]);
  const loaderStore = useLoaderStore();
  const messageStore = useMessageStore();

  onMounted(async () => {
    isLayoutReady.value = true;
    users.value = await fetchUsers();
  });

  function onReady(editor) {
    [...editorWordCount.value.children].forEach(child => child.remove());

    // [...editorMenuBar.value.children].forEach(child => child.remove());

    const wordCount = editor.plugins.get('WordCount');
    editorWordCount.value.appendChild(wordCount.wordCountContainer);
    // editorMenuBar.value.appendChild(editor.ui.view.menuBarView.element);
  }

  watch(() => props.event, (newEvent) => {
    if (newEvent) {
      event.value = {
        title: newEvent.title || '',
        location: newEvent.location || '',
        type: newEvent.type || 'private',
        description: newEvent.description || '',
        date: newEvent ? [newEvent.startDate, newEvent.endDate] : null,
        file: newEvent.id ? `event_${newEvent.id}.pdf` : null,
        collaborators: users.value.filter(user => newEvent.collaborators.includes(user.key))
      };
    }
  });

  const close = () => {
    emit('toggle-form'); // Emit toggle-form event to close the form
  };

  const fetchUsers = async () => {
    const response = await axios.get('/api/users');

    if(response && response.status === 200) {
      return response.data.users.filter(user => user.id !== JSON.parse(localStorage.getItem('user')).id).map(user => {
        return {
          key: user.id,
          value: `${user.first_name} ${user.last_name}`
        }
      });
    }
  }

  const addFile = (e) => {
    event.value.file = e.target.files[0];
  }

  const submitForm = async (e) => {
    e.preventDefault();

    let url = '';
    let headers = {};

    if(props.event) {
      url = `/api/event/update/${props.event.id}`;
      headers = {
        'Content-Type': 'application/json'
      }
    } else {
      url = '/api/event/create';
      headers = {
        'Content-Type': 'multipart/form-data'
      }
    }

    loaderStore.setLoader(true);

    await axios.post(url, {
      title: event.value.title,
      description: event.value.description,
      location: event.value.location,
      start_at: event.value.date[0],
      end_at: event.value.date[1],
      type: event.value.type,
      collaborated_users: event.value.collaborators,
      file: event.value.file,
      created_by: JSON.parse(localStorage.getItem('user')).id
    }, {
      headers: headers
    }).then((res) => {
      if(res.status === 200) {
        loaderStore.setLoader(false);
        messageStore.setMessage(res.data.message);
        event.value = {
          title: '',
          location: '',
          type: 'private',
          description: '',
          date: null,
          file: null,
          collaborators: []
        };
        emit('update-events', res.data.event);
        close();
      }
    }). catch(error => {
      loaderStore.setLoader(false);
      console.log(error);
    });
  }
</script>

<template>
  <Transition name="slide">
    <section v-if="isVisible" class="form-container">
      <template v-if="success">
        <Button class="p-4 icon-button" type="button" @click="close" colour="bg-violet" text-color="white">
          <font-awesome-icon icon="xmark" />
        </Button>
        <form>
          <Input v-model="event.title" type="text" placeholder="Title" :required="true" />
          <Location v-model="event.location" placeholder="Location" />
          <div class="input-type-wrapper flex flex-row justify-start align-center gap-4">
            <div class="flex flex-row justify-start align-center gap-2">
              <Input name="type" v-model="event.type" type="radio" value="private" :required="true" />
              <label for="private-type">Private</label>
            </div>
            <div class="flex flex-row justify-start align-center gap-2">
              <Input name="type" v-model="event.type" type="radio" value="public" :required="true" />
              <label for="public-type">Public</label>
            </div>
          </div>
          <VueDatePicker v-model="event.date"
                         range
                         dark
                         position="left"
                         auto-position="bottom"
                         :clearable="true"
                         :enable-time-picker="true"
                         :auto-apply="true"
                         :text-input="false"
                         placeholder="Select the dates"
                         :ui="{
                         input: 'date-input',
                         calendarCell: 'date-calendar-cell'
                       }" />
          <div class="main-container">
            <div class="editor-container editor-container_classic-editor editor-container_include-word-count" ref="editorContainerElement">
              <div class="editor-container__editor">
                <div ref="editorElement">
                  <ckeditor v-if="editor && config" v-model="event.description" :editor="editor" :config="config" @ready="onReady" />
                </div>
              </div>
              <div class="editor_container__word-count" ref="editorWordCountElement"></div>
            </div>
          </div>
          <Input v-if="!props.event"
                 type="file"
                 accept=".pdf"
                 placeholder="Upload PDF"
                 @change="addFile" />
          <Multiselect v-model="event.collaborators"
                       class="multiselect"
                       :multiple="true"
                       :options="users"
                       placeholder="Share event with user"
                       openDirection="below"
                       label="value"
                       track-by="key"
                       :required="true"
                       :searchable="true"
                       :preserve-search="true"
                       :close-on-select="false"
                       :clear-on-select="false">
          </Multiselect>
          <Button class="mt-4 ml-auto mr-0"
                  type="button"
                  colour="bg-violet"
                  text-color="white"
                  @click="submitForm">
            Submit
          </Button>
        </form>
      </template>
    </section>
  </Transition>
</template>

<style scoped>
  .form-container {
    position: relative;
    max-width: 650px;
    display: flex;
    flex-flow: column nowrap;
    justify-content: center;
    align-items: end;
    right: 0;
    padding: 2rem;
  }
  form {
    width: 100%;
    margin-top: 2rem;
  }
  .input-type-wrapper {
    margin-bottom: 1rem;
  }
  .input-type-wrapper .input-wrapper {
    margin-bottom: 0;
  }
  .slide-enter-active,
  .slide-leave-active {
    transition: right 0.3s ease-out;
  }
  .slide-enter-from,
  .slide-leave-to {
    right: -100%;
  }
</style>
