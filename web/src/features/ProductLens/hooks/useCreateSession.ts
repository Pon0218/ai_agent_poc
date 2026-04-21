import { createMutation } from '@tanstack/svelte-query';
import { createSession } from '../api/sessions';

export const useCreateSession = () => {
	return createMutation(() => ({
		mutationFn: createSession
	}));
};
