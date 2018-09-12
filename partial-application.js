
function partialApplication(func) {
  // partial application returns a new version of the func
  return function(...args) {
    // we have access to func.length due to closure
    if (args.length >= func.length) {
      // we have all the arguments we need to execute, so we will execute
      return func(...args)
    } else {
      // we have some, but not all the arguments we need
      // the bind method returns a new function with reduced arity
      return partialApplication(func.bind(null, ...args))
    }
  }
}
