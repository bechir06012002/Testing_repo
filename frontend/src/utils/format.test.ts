import { test } from 'node:test';
import assert from 'node:assert/strict';
import { formatCents, truncate } from './format';

test('formatCents formats whole dollars', () => {
  assert.equal(formatCents(1000), '$10.00');
});

test('formatCents formats cents', () => {
  assert.equal(formatCents(1050), '$10.50');
});

test('truncate leaves short strings alone', () => {
  assert.equal(truncate('hi', 10), 'hi');
});

test('truncate cuts long strings and adds an ellipsis', () => {
  assert.equal(truncate('hello world', 5), 'hello...');
});
