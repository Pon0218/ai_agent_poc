import { createMutation } from '@tanstack/svelte-query';
import { callAnonymizedChat } from '../api/anonymized-chat';

export const useAnonymizedChat = () => {
	return createMutation(() => ({
		mutationFn: callAnonymizedChat
		// onSuccess: (data) => { ... }  // Add global side effects here if needed
		// onError: (error) => { ... }   // e.g. global toast, logging
	}));
};
