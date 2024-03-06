import kue from "kue";

const queue = kue.createQueue();

const blackListedPhoneNumbers = [
    "4153518780",
    "4153518781"
];

function sendNotification(phoneNumber, message, job, done) {
    const total = 100;
    job.progress(0, total);

    if (blackListedPhoneNumbers.includes(phoneNumber)) {
        return done(Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    job.progress(50, total)
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

queue.process("push_notification_code_2", 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
