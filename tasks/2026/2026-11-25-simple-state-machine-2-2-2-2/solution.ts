export type StateMachineTransition<S extends string, E extends string> = {
  readonly from: S;
  readonly event: E;
  readonly to: S;
};

export interface StateMachineConfig<S extends string, E extends string> {
  readonly initial: S;
  readonly states: readonly S[];
  readonly transitions: readonly StateMachineTransition<S, E>[];
}

export interface StateMachine<S extends string, E extends string> {
  getState(): S;
  transition(event: E): S;
  can(event: E): boolean;
  reset(): void;
}

function assertValidConfig<S extends string, E extends string>(
  config: StateMachineConfig<S, E>
): void {
  const { initial, states, transitions } = config;

  if (!states.includes(initial)) {
    throw new Error(`Initial state ${JSON.stringify(initial)} is not listed in states.`);
  }

  for (const transition of transitions) {
    if (!states.includes(transition.from)) {
      throw new Error(`Transition from ${JSON.stringify(transition.from)} is not a known state.`);
    }

    if (!states.includes(transition.to)) {
      throw new Error(`Transition to ${JSON.stringify(transition.to)} is not a known state.`);
    }
  }
}

export function createStateMachine<S extends string, E extends string>(
  config: StateMachineConfig<S, E>
): StateMachine<S, E> {
  assertValidConfig(config);

  let current: S = config.initial;

  return {
    getState() {
      return current;
    },

    can(event: E): boolean {
      return config.transitions.some(
        (transition) => transition.from === current && transition.event === event
      );
    },

    transition(event: E): S {
      const transition = config.transitions.find(
        (candidate) => candidate.from === current && candidate.event === event
      );

      if (!transition) {
        throw new Error(
          `Cannot transition from ${JSON.stringify(current)} with event ${JSON.stringify(event)}`
        );
      }

      current = transition.to;
      return current;
    },

    reset(): void {
      current = config.initial;
    },
  };
}
