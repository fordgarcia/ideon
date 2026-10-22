// notes
const note_inputs = new Map()

note_inputs.set('header', document.querySelector('#id_header'));
note_inputs.set('content', document.querySelector('#id_content'));
note_inputs.set('select', document.querySelector('#id_topic'));
if (note_inputs.get('select')) note_inputs.set('selected', note_inputs.get('select').querySelector('option:checked'));

if (note_inputs.get('header')) note_inputs.get('header').placeholder = 'What is this?';
if (note_inputs.get('content')) note_inputs.get('content').placeholder = 'EUREKA!';
if (note_inputs.get('selected')) note_inputs.get('selected').textContent = 'TOPIC';


// lesson
const lesson_inputs = new Map()

lesson_inputs.set('name', document.querySelector('#id_lesson_name'));
lesson_inputs.set('description', document.querySelector('#id_lesson_description'));

if (lesson_inputs.get('name')) lesson_inputs.get('name').placeholder = 'Lesson';
if (lesson_inputs.get('name')) lesson_inputs.get('description').placeholder = 'Description';


// topic 
const topic_inputs = new Map()

topic_inputs.set('name', document.querySelector('#id_topic_name'));
topic_inputs.set('description', document.querySelector('#id_topic_description'));

if (topic_inputs.get('name')) topic_inputs.get('name').placeholder = 'Topic';
if (topic_inputs.get('description')) topic_inputs.get('description').placeholder = 'Description';








































// const headerInput = document.querySelector('#id_header');
// const contentInput = document.querySelector('#id_content');
// const selectInput = document.querySelector('#id_topic');
// const selectedInput = selectInput.querySelector('option:checked');

// selectedInput.textContent = 'TOPIC';
// headerInput.placeholder = 'What is this?';
// contentInput.placeholder = 'EUREKA!';