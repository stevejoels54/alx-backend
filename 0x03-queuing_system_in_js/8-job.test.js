import kue from "kue";
import { expect } from "chai";
import createPushNotificationsJobs from "./8-job";

const queue = kue.createQueue();

describe("createPushNotificationsJobs", function () {
    beforeEach(function () {
    queue.testMode.enter();
    });

    afterEach(function () {
    queue.testMode.clear();
    });

    after(() => {
    queue.testMode.exit();
    });

    it("validates jobs is an array", function () {
        expect(() => createPushNotificationsJobs("test", queue)).to.throw(
        "Jobs is not an array"
        );
    });

    it("validates the job and creates it", function () {
    const list = [
        {
        phoneNumber: "4153518780",
        message: "This is the code 1234 to verify your account",
        },
    ];
    createPushNotificationsJobs(list, queue);
    });
});
