beforeAll(() => {
  window.HTMLElement.prototype.scrollIntoView = function () {};
});

import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders chatbot title", () => {
  render(<App />);
  const title = screen.getByText(/AI Assistant/i);
  expect(title).toBeInTheDocument();
});

test("input box exists", () => {
  render(<App />);
  const input = screen.getByPlaceholderText(/Ask something/i);
  expect(input).toBeInTheDocument();
});

test("send button exists", () => {
  render(<App />);
  const button = screen.getByText(/Send/i);
  expect(button).toBeInTheDocument();
});