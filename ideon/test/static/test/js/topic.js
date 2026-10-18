
// const topicsContainer = document.querySelector("#topics");

// async function loadTopics() {
//     try {
//         const response = await fetch("/api/topics/");

//         if (!response.ok) {
//             throw new Error(`HTTP error: ${response.status}`);
//         }

//         const topics = await response.json();

//         topics.forEach(topic => {
//             const article = document.createElement("article");
//             const heading = document.createElement("h2");
//             const notesList = document.createElement("ul");

//             heading.textContent = topic.title;

//             topic.notes.forEach(note => {
//                 const item = document.createElement("li");
//                 item.textContent = note.content;
//                 notesList.appendChild(item);
//             });

//             article.append(heading, notesList);
//             topicsContainer.appendChild(article);
//         });
//     } catch (error) {
//         console.error("Failed to load topics:", error);
//         topicsContainer.textContent = "Failed to load topics.";
//     }
// }

// loadTopics();

const topicsContainer = document.querySelector("#container");

let hasTopic = false;

async function getTopic(topic_id) {
    try {
        const response = await fetch(`../api/topic/${topic_id}`);

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        } else {
            // if (!hasTopic) {
            //     const topic = await response.json();

            //     const article = document.createElement('article');
            //     const heading = document.createElement('h1');
            //     const text = document.createElement('p');

            //     heading.textContent = topic['name'];
            //     text.textContent = topic['description'];

            //     article.append(heading, text);
            //     topicsContainer.append(article);
            //     hasTopic = true;
            // } else {
            //     topicsContainer.replaceChildren();
            //     hasTopic = false;
            // }
            const topic = await response.json();

            const article = document.createElement('article');
            const heading = document.createElement('h1');
            const text = document.createElement('p');

            heading.textContent = topic['name'];
            heading.id = 'topic_name'
            text.textContent = topic['description'];
            text.className = 'texts';

            article.append(heading, text);
            topicsContainer.replaceChildren(article);
        }

    } catch (error) {

    }
}

async function getLesson(lesson_id) {
    try {
        const response = await fetch(`../api/lesson/${lesson_id}`);

        if (!response.ok) {
            throw new Error(`HTTP error: ${lesson.status}`);
        }

        const lesson = await response.json();

        const article = document.createElement('article');
        const heading = document.createElement('h1');
        const heading_description = document.createElement('p');

        heading.id = 'lesson_name';
        heading.textContent = lesson['name'];

        heading_description.textContent = lesson['description'];
        heading_description.id = 'lesson_description';

        article.append(heading, heading_description);
        
        const objects = {};

        for (const [key, value] of Object.entries(lesson)) {
            if (value !== null && typeof value === "object") {
                objects[key] = [
                    document.createElement('h3'),
                    document.createElement('p')
                ];
                objects[key][0].textContent = value.name;
                objects[key][1].textContent = value.description;
                objects[key][1].className = 'texts';
                article.append(objects[key][0], objects[key][1]);
            }
        }

        topicsContainer.replaceChildren(article);


    } catch (error) {

    }
}