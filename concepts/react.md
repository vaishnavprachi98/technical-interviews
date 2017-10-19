# React/Redux Questions

## When should you use functional React components over classes?
- When you don't need to manage states, and
- when you don't need to use the React lifecycle

## Why do we use Redux when React already handles state?
- When the parent needs to access the child's state and the child's the parent's state at the same time.
- Simplfies the state, as Redux places some constraints and conventions
- When the state grows too large in a stateful component (a.k.a container), it is better to separate the state from the React components
- Want to access state from a sibling component, but don't want to move state up into common ancestor
- Easier to move React/Redux containers around the codebase
- Don't have to pass props down to children and grandchildren in React components that are deeply nested in the component hierarchy

## What are some of the disadvantages of using redux?
- still can write terrible code (not a silver bullet)
    - Javascript is not a immutable language
    - Parts of redux architecture might be handling too much responsibility
- lots of "boilerplate" code
- unnecessary for handling UI state

## How much responsibility should be placed in action creators, reducers and React components?
- Most business logic (if not all) should go in the action creators
- Reducers should pass payload into the `store`
- React components should be broken into two parts: container and presentational components
    - Presentational components have no redux code at all, and should only be concerned with how it looks on the screen
    - Containers should only wrap presentational components (supplying them with props), contain selector functions (e.g. mapStateToProps) and connect React with redux store and dispatcher

## What is the React lifecycle?
    ![diagram](https://s3.amazonaws.com/codementor_content/2016-Jul/reactjs-qs1.png)

## Draw the React cycle when it updates a component.
1. `componentWillReceiveProps()`
2. `shouldComponentUpdate()`
3. `componentWillUpdate()`
4. `render()`
5. `componentDidUpdate()`

Note: Material taken from monPlan summer 2017 coding interviews.