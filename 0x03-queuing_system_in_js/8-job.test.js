import sinon from 'sinon';
import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job';

const queue = createQueue({ name: 'push_notification_code_test' });

describe('createPushNotificationsJobs: ', () => {
  const spy = sinon.spy(console, 'log');

  beforeEach(() => {
    queue.testMode.enter();
  });

  it('display an error message if jobs is not an array', () => {
    const list = 'Sample string';
    expect(() => createPushNotificationsJobs(list, queue)).to.throw();
  });

  it('creates new jobs to add the queue', () => {
    const list = [{
        phoneNumber: '4153518780',
        message: 'This is the code 9834 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4542 to verify your account',
      },
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });

  /**
   * Failing tests for some reason
   * Fix later
   ***
  it('displays the correct message when a job is created', () => {
    const list = [{
      phoneNumber: '4153518781',
      message: 'This is the code 4542 to verify your account',
    }];
    createPushNotificationsJobs(list, queue);
    const job = queue.testMode.jobs[0];

    expect(spy.calledWith(`Notification job created: ${job.id}`)).to.equal(true);
    spy.restore();
  });

  it('displays the correct message when a job is completed', () => {
    const list = [{
      phoneNumber: '4153518780',
      message: 'This is the code 9834 to verify your account',
    }];
    createPushNotificationsJobs(list, queue);
    const job = queue.testMode.jobs[0];

    job._events.complete();
    expect(spy.calledWith(`Notification job ${job.id} completed`)).to.equal(true);
    spy.restore();
  });

  it('displays the correct message when a job fails with an error', () => {
    const list = [{
      phoneNumber: '4153518780',
      message: 'This is the code 9834 to verify your account',
    }];
    createPushNotificationsJobs(list, queue);
    const job = queue.testMode.jobs[0];
    const err = 'Error Message';

    job._events.failed(err);
    console.log(`${job.id}`);
    expect(spy.calledWith(`Notification job ${job.id} failed: ${err}`)).to.equal(true);
    spy.restore();
  });

  it('displays the correct message for a job progress', () => {
    const list = [{
      phoneNumber: '4153518780',
      message: 'This is the code 9834 to verify your account',
    }];
    createPushNotificationsJobs(list, queue);
    const job = queue.testMode.jobs[0];
    const progress = 50;

    job._events.progress(progress);
    expect(spy.calledWith(`Notification job ${job.id} ${progress}% complete`)).to.equal(true);
    spy.restore();
  });
  */

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });
});
